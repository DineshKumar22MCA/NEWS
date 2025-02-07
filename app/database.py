from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
'''
 Connecting to the docker container
    - If you application is running in the host machine,
      then,
       -  the host_ip can be localhost:3307,
       -  ip_address_of_the_mysql_container:3306

    - If you running the server as a docker container,
       - container_id[mysql]: 3306 [ when run through compose file ]
       - ip_address_of_the_mysql_container:3306
'''
# DATABASE_URL = "mysql+pymysql://root:root@mysql:3307/mydb" #for doc

# DATABASE_URL = "mysql+pymysql://root:root@localhost/mydb" #for local

DATABASE_HOST = os.getenv("DATABASE_HOST","localhost")
print(DATABASE_HOST)
DATABASE_URL = f"mysql+pymysql://root:root@{DATABASE_HOST}/mydb"

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False,autoflush=False , bind=engine)


Base = declarative_base()

