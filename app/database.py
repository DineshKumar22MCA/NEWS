from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
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


# DATABASE_HOST = os.getenv("DATABASE_HOST","localhost")

# DATABASE_URL = f"mysql+pymysql://wsl_root:password@172.29.16.1/mydb"


dotenv_path = os.path.join(os.path.dirname(__file__), "../env/.db")
load_dotenv(dotenv_path)

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_DB = os.getenv("DATABASE_DB")

DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_DB}"

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False,autoflush=False , bind=engine)


Base = declarative_base()

