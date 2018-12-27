１．必要モジュール

pip install requests -t .
pip install cx_Oracle -t .
※cx_OracleはLinux版でなければならないのでLinuxからpipを実行する。
　cx_Oracle.cpython-36m-x86_64-linux-gnu.so


２．必要ディレクトリ

./lib


３．必要ツール
OracleクライアントとSDKをlib直下に格納する。

https://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html

instantclient-basiclite-linux.x64-12.1.0.2.0.zip
instantclient-sqlplus-linux.x64-12.1.0.2.0.zip
instantclient-sdk-linux.x64-12.1.0.2.0.zip

４．環境変数
lambdaの環境変数として定義する。

REGION　　　　※リージョン名
dbname　　　　※RDSインスタンス名
endpoint　　　※RDSエンドポイント
my_db　　　　 ※DB名
password　　　※RDSパスワード
s3bucket　　　※格納先バケット名
search_word　※ログ名を検索するワード（部分一致）
user　　　　　※RDSユーザ

※参考：動作しているlambda関数のtree
.
├── INSTALLER
├── METADATA
├── README.md
├── RECORD
├── WHEEL
├── bin
│   └── chardetect.exe
├── certifi
│   ├── __init__.py
│   ├── __main__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── __main__.cpython-37.pyc
│   │   └── core.cpython-37.pyc
│   ├── cacert.pem
│   └── core.py
├── certifi-2018.11.29.dist-info
│   ├── DESCRIPTION.rst
│   ├── INSTALLER
│   ├── LICENSE.txt
│   ├── METADATA
│   ├── RECORD
│   ├── WHEEL
│   ├── metadata.json
│   └── top_level.txt
├── chardet
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── big5freq.cpython-37.pyc
│   │   ├── big5prober.cpython-37.pyc
│   │   ├── chardistribution.cpython-37.pyc
│   │   ├── charsetgroupprober.cpython-37.pyc
│   │   ├── charsetprober.cpython-37.pyc
│   │   ├── codingstatemachine.cpython-37.pyc
│   │   ├── compat.cpython-37.pyc
│   │   ├── cp949prober.cpython-37.pyc
│   │   ├── enums.cpython-37.pyc
│   │   ├── escprober.cpython-37.pyc
│   │   ├── escsm.cpython-37.pyc
│   │   ├── eucjpprober.cpython-37.pyc
│   │   ├── euckrfreq.cpython-37.pyc
│   │   ├── euckrprober.cpython-37.pyc
│   │   ├── euctwfreq.cpython-37.pyc
│   │   ├── euctwprober.cpython-37.pyc
│   │   ├── gb2312freq.cpython-37.pyc
│   │   ├── gb2312prober.cpython-37.pyc
│   │   ├── hebrewprober.cpython-37.pyc
│   │   ├── jisfreq.cpython-37.pyc
│   │   ├── jpcntx.cpython-37.pyc
│   │   ├── langbulgarianmodel.cpython-37.pyc
│   │   ├── langcyrillicmodel.cpython-37.pyc
│   │   ├── langgreekmodel.cpython-37.pyc
│   │   ├── langhebrewmodel.cpython-37.pyc
│   │   ├── langhungarianmodel.cpython-37.pyc
│   │   ├── langthaimodel.cpython-37.pyc
│   │   ├── langturkishmodel.cpython-37.pyc
│   │   ├── latin1prober.cpython-37.pyc
│   │   ├── mbcharsetprober.cpython-37.pyc
│   │   ├── mbcsgroupprober.cpython-37.pyc
│   │   ├── mbcssm.cpython-37.pyc
│   │   ├── sbcharsetprober.cpython-37.pyc
│   │   ├── sbcsgroupprober.cpython-37.pyc
│   │   ├── sjisprober.cpython-37.pyc
│   │   ├── universaldetector.cpython-37.pyc
│   │   ├── utf8prober.cpython-37.pyc
│   │   └── version.cpython-37.pyc
│   ├── big5freq.py
│   ├── big5prober.py
│   ├── chardistribution.py
│   ├── charsetgroupprober.py
│   ├── charsetprober.py
│   ├── cli
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   └── chardetect.cpython-37.pyc
│   │   └── chardetect.py
│   ├── codingstatemachine.py
│   ├── compat.py
│   ├── cp949prober.py
│   ├── enums.py
│   ├── escprober.py
│   ├── escsm.py
│   ├── eucjpprober.py
│   ├── euckrfreq.py
│   ├── euckrprober.py
│   ├── euctwfreq.py
│   ├── euctwprober.py
│   ├── gb2312freq.py
│   ├── gb2312prober.py
│   ├── hebrewprober.py
│   ├── jisfreq.py
│   ├── jpcntx.py
│   ├── langbulgarianmodel.py
│   ├── langcyrillicmodel.py
│   ├── langgreekmodel.py
│   ├── langhebrewmodel.py
│   ├── langhungarianmodel.py
│   ├── langthaimodel.py
│   ├── langturkishmodel.py
│   ├── latin1prober.py
│   ├── mbcharsetprober.py
│   ├── mbcsgroupprober.py
│   ├── mbcssm.py
│   ├── sbcharsetprober.py
│   ├── sbcsgroupprober.py
│   ├── sjisprober.py
│   ├── universaldetector.py
│   ├── utf8prober.py
│   └── version.py
├── chardet-3.0.4.dist-info
│   ├── DESCRIPTION.rst
│   ├── INSTALLER
│   ├── METADATA
│   ├── RECORD
│   ├── WHEEL
│   ├── entry_points.txt
│   ├── metadata.json
│   └── top_level.txt
├── cx_Oracle-7.0.0.dist-info
│   ├── INSTALLER
│   ├── METADATA
│   ├── RECORD
│   ├── WHEEL
│   └── top_level.txt
├── cx_Oracle.cpython-36m-x86_64-linux-gnu.so
├── idna
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── codec.cpython-37.pyc
│   │   ├── compat.cpython-37.pyc
│   │   ├── core.cpython-37.pyc
│   │   ├── idnadata.cpython-37.pyc
│   │   ├── intranges.cpython-37.pyc
│   │   ├── package_data.cpython-37.pyc
│   │   └── uts46data.cpython-37.pyc
│   ├── codec.py
│   ├── compat.py
│   ├── core.py
│   ├── idnadata.py
│   ├── intranges.py
│   ├── package_data.py
│   └── uts46data.py
├── idna-2.8.dist-info
│   ├── INSTALLER
│   ├── LICENSE.rst
│   ├── METADATA
│   ├── RECORD
│   ├── WHEEL
│   └── top_level.txt
├── lambda_function.py
├── lib
│   ├── BASIC_LITE_README
│   ├── SQLPLUS_README
│   ├── adrci
│   ├── genezi
│   ├── glogin.sql
│   ├── libaio.so.1
│   ├── libclntsh.so.12.1
│   ├── libclntshcore.so.12.1
│   ├── libipc1.so
│   ├── libmql1.so
│   ├── libnnz12.so
│   ├── libocci.so.12.1
│   ├── libociicus.so
│   ├── libocijdbc12.so
│   ├── libons.so
│   ├── liboramysql12.so
│   ├── libsqlplus.so
│   ├── libsqlplusic.so
│   ├── ojdbc6.jar
│   ├── ojdbc7.jar
│   ├── sdk
│   │   ├── SDK_README
│   │   ├── admin
│   │   │   └── oraaccess.xsd
│   │   ├── demo
│   │   │   ├── cdemo81.c
│   │   │   ├── demo.mk
│   │   │   ├── occidemo.sql
│   │   │   ├── occidemod.sql
│   │   │   ├── occidml.cpp
│   │   │   ├── occiobj.cpp
│   │   │   ├── occiobj.typ
│   │   │   ├── oraaccess.xml
│   │   │   └── setuporamysql.sh
│   │   ├── include
│   │   │   ├── ldap.h
│   │   │   ├── nzerror.h
│   │   │   ├── nzt.h
│   │   │   ├── occi.h
│   │   │   ├── occiAQ.h
│   │   │   ├── occiCommon.h
│   │   │   ├── occiControl.h
│   │   │   ├── occiData.h
│   │   │   ├── occiObjects.h
│   │   │   ├── oci.h
│   │   │   ├── oci1.h
│   │   │   ├── oci8dp.h
│   │   │   ├── ociap.h
│   │   │   ├── ociapr.h
│   │   │   ├── ocidef.h
│   │   │   ├── ocidem.h
│   │   │   ├── ocidfn.h
│   │   │   ├── ociextp.h
│   │   │   ├── ocikpr.h
│   │   │   ├── ocixmldb.h
│   │   │   ├── ocixstream.h
│   │   │   ├── odci.h
│   │   │   ├── oratypes.h
│   │   │   ├── ori.h
│   │   │   ├── orid.h
│   │   │   ├── orl.h
│   │   │   ├── oro.h
│   │   │   ├── ort.h
│   │   │   └── xa.h
│   │   ├── ott
│   │   └── ottclasses.zip
│   ├── sqlplus
│   ├── uidrvci
│   └── xstreams.jar
├── requests
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── __version__.cpython-37.pyc
│   │   ├── _internal_utils.cpython-37.pyc
│   │   ├── adapters.cpython-37.pyc
│   │   ├── api.cpython-37.pyc
│   │   ├── auth.cpython-37.pyc
│   │   ├── certs.cpython-37.pyc
│   │   ├── compat.cpython-37.pyc
│   │   ├── cookies.cpython-37.pyc
│   │   ├── exceptions.cpython-37.pyc
│   │   ├── help.cpython-37.pyc
│   │   ├── hooks.cpython-37.pyc
│   │   ├── models.cpython-37.pyc
│   │   ├── packages.cpython-37.pyc
│   │   ├── sessions.cpython-37.pyc
│   │   ├── status_codes.cpython-37.pyc
│   │   ├── structures.cpython-37.pyc
│   │   └── utils.cpython-37.pyc
│   ├── __version__.py
│   ├── _internal_utils.py
│   ├── adapters.py
│   ├── api.py
│   ├── auth.py
│   ├── certs.py
│   ├── compat.py
│   ├── cookies.py
│   ├── exceptions.py
│   ├── help.py
│   ├── hooks.py
│   ├── models.py
│   ├── packages.py
│   ├── sessions.py
│   ├── status_codes.py
│   ├── structures.py
│   └── utils.py
├── requests-2.21.0.dist-info
│   ├── INSTALLER
│   ├── LICENSE
│   ├── METADATA
│   ├── RECORD
│   ├── WHEEL
│   └── top_level.txt
├── sample
│   └── downloadlogs.py
├── top_level.txt
├── tree.txt
├── urllib3
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── _collections.cpython-37.pyc
│   │   ├── connection.cpython-37.pyc
│   │   ├── connectionpool.cpython-37.pyc
│   │   ├── exceptions.cpython-37.pyc
│   │   ├── fields.cpython-37.pyc
│   │   ├── filepost.cpython-37.pyc
│   │   ├── poolmanager.cpython-37.pyc
│   │   ├── request.cpython-37.pyc
│   │   └── response.cpython-37.pyc
│   ├── _collections.py
│   ├── connection.py
│   ├── connectionpool.py
│   ├── contrib
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   ├── _appengine_environ.cpython-37.pyc
│   │   │   ├── appengine.cpython-37.pyc
│   │   │   ├── ntlmpool.cpython-37.pyc
│   │   │   ├── pyopenssl.cpython-37.pyc
│   │   │   ├── securetransport.cpython-37.pyc
│   │   │   └── socks.cpython-37.pyc
│   │   ├── _appengine_environ.py
│   │   ├── _securetransport
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-37.pyc
│   │   │   │   ├── bindings.cpython-37.pyc
│   │   │   │   └── low_level.cpython-37.pyc
│   │   │   ├── bindings.py
│   │   │   └── low_level.py
│   │   ├── appengine.py
│   │   ├── ntlmpool.py
│   │   ├── pyopenssl.py
│   │   ├── securetransport.py
│   │   └── socks.py
│   ├── exceptions.py
│   ├── fields.py
│   ├── filepost.py
│   ├── packages
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-37.pyc
│   │   │   └── six.cpython-37.pyc
│   │   ├── backports
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-37.pyc
│   │   │   │   └── makefile.cpython-37.pyc
│   │   │   └── makefile.py
│   │   ├── six.py
│   │   └── ssl_match_hostname
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       │   ├── __init__.cpython-37.pyc
│   │       │   └── _implementation.cpython-37.pyc
│   │       └── _implementation.py
│   ├── poolmanager.py
│   ├── request.py
│   ├── response.py
│   └── util
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-37.pyc
│       │   ├── connection.cpython-37.pyc
│       │   ├── queue.cpython-37.pyc
│       │   ├── request.cpython-37.pyc
│       │   ├── response.cpython-37.pyc
│       │   ├── retry.cpython-37.pyc
│       │   ├── ssl_.cpython-37.pyc
│       │   ├── timeout.cpython-37.pyc
│       │   ├── url.cpython-37.pyc
│       │   └── wait.cpython-37.pyc
│       ├── connection.py
│       ├── queue.py
│       ├── request.py
│       ├── response.py
│       ├── retry.py
│       ├── ssl_.py
│       ├── timeout.py
│       ├── url.py
│       └── wait.py
└── urllib3-1.24.1.dist-info
    ├── INSTALLER
    ├── LICENSE.txt
    ├── METADATA
    ├── RECORD
    ├── WHEEL
    └── top_level.txt

37 directories, 328 files
