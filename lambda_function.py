import cx_Oracle
import logging
import sys, os, base64, datetime, hashlib, hmac, urllib, boto3
from boto3 import session
from botocore.exceptions import ClientError
from base64 import b64decode
import time
import requests

def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()
 
def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning

def lambda_handler(event, context):
    sys.path.append('./lib')
    os.environ["LD_LIBRARY_PATH"] += ":./lib"
    os.environ["ORACLE_HOME"] = "/var/task"
    os.environ["NLS_LANG"] = "Japanese_Japan.AL32UTF8"
    os.environ["LOCALDOMAIN"] ='ap-northeast-1.compute.internal'

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    con = cx_Oracle.connect(os.environ["user"], os.environ["password"], os.environ["endpoint"] + "/" + os.environ["my_db"])
    cur = con.cursor()

    logger.info("connect RDS : " + os.environ["my_db"])

    #create_statspack_report
    result = cur.execute("""
        DECLARE
            vBSnapID     INTEGER;
            vESnapID     INTEGER;
        BEGIN
            select (select max(snap_id) from stats$snapshot where snap_id !=(select max(snap_id) from stats$snapshot)), (select max(snap_id)  from stats$snapshot) into vBSnapID, vESnapID  from dual;
            RDSADMIN.RDS_RUN_SPREPORT(vBSnapID,vESnapID);
        END;
    """)
    con.close()

    logger.info("disconect RDS" + os.environ["my_db"])

    #put_statspack_report
    client_rds = boto3.client('rds')

    #describe RDS
    SINCE = datetime.datetime.now().replace(minute=0,second=0,microsecond=0) - datetime.timedelta(hours=1)
    SINCE_U = int(time.mktime(SINCE.timetuple())) * 1000

    files = client_rds.describe_db_log_files(
    DBInstanceIdentifier= os.environ["dbname"],
    FilenameContains= os.environ["search_word"],
    FileLastWritten = SINCE_U
    )

    #create backet path
    maindir = datetime.datetime.now().strftime('%Y%m')
    subdir = datetime.datetime.now().strftime('%Y%m%d')

    # S3情報
    resource_s3 = boto3.resource('s3')
    bucket_name = os.environ["s3bucket"]
    bucket_s3 = resource_s3.Bucket(bucket_name)
    
    # Request用セッション情報
    s = session.Session()
    cred = s.get_credentials()
    access_key = cred.access_key
    secret_key = cred.secret_key
    session_token = cred.token

    for logs in files["DescribeDBLogFiles"]:
        LOGFILE_NAME = logs["LogFileName"]
        new_LOGFILE_NAME = LOGFILE_NAME.replace('/', '_')

        logger.info("以下ファイルをダウンロードします。：" + LOGFILE_NAME)

        # logfile download for requests
        if access_key is None or secret_key is None or session_token is None:
            print("Credentials are not available.")
            sys.exit()
        
        # Request用パラメータ生成
        method = 'GET'
        service = 'rds'
        uri = '/v13/downloadCompleteLogFile/' + os.environ["dbname"] + '/' + LOGFILE_NAME
        host = 'rds.' + os.environ["REGION"] + '.amazonaws.com'
        rds_endpoint = 'https://' + host
        endpoint =  rds_endpoint + uri

        t = datetime.datetime.utcnow()
        amzdate = t.strftime('%Y%m%dT%H%M%SZ')
        datestamp = t.strftime('%Y%m%d')
        canonical_uri = uri 

        # 認証情報生成
        canonical_headers = 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n'
        signed_headers = 'host;x-amz-date'
        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = datestamp + '/' + os.environ["REGION"] + '/' + service + '/' + 'aws4_request'
        canonical_querystring = ''

        payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()
        canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
        string_to_sign = algorithm + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

        signing_key = getSignatureKey(secret_key, datestamp, os.environ["REGION"], service)
        signature = hmac.new(signing_key, (string_to_sign).encode("utf-8"), hashlib.sha256).hexdigest()

        authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature
        headers = {'Accept-Encoding':'gzip', 'x-amz-date':amzdate, 'x-amz-security-token':session_token, 'Authorization':authorization_header}

        # Request発行
        r = requests.get(endpoint, headers=headers, stream=True)

        #rds_response = rds_response["LogFileData"]

        putfilename = "/tmp/" + new_LOGFILE_NAME 
        with open(putfilename, 'wb') as f:
            for part in r.iter_content(chunk_size=8192):
                f.write(part)

        #s3 cp for lambda
        puts3_filename = maindir + "/" + subdir + "/" + new_LOGFILE_NAME
        bucket_s3.upload_file(putfilename, puts3_filename)

        logger.info("s3 upload ok : " + puts3_filename)

    logger.info("end job!!")


if __name__ == "__main__":
    pass