
from sqlalchemy import Column ,Integer , String
from app.database import Base


class Query(Base):
    __tablename__ = "queries"

    query_id = Column(Integer, primary_key=True,index=True,autoincrement=True)
    query_name = Column (String(255), index=True)