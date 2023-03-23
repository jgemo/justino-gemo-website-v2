#import sqlalchemy
#print(sqlalchemy.__version__)
#pip install pymysql

from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://yv0s1zbe7x4qmlbpbawz:pscale_pw_o1GnuKRRMuEkxMSTKgrq13L7W2e15KD7fx4PFtAnyNC@ap-southeast.connect.psdb.cloud/jgemo?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

result_dicts = []
for row in result.all():
    result_dicts.append(dict(row))

print(result_dicts)
