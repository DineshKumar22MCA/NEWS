# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os

# # SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@mysql:3306/mydb"

# # SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost/mydb"

# DATABASE_HOST = os.getenv("DATABASE_HOST","localhost")
# SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://wsl_root:password@172.29.16.1:3306/mydb"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base = declarative_base()