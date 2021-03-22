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

