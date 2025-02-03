
from pydantic import BaseModel
# from datetime import datetime

class QueryBase(BaseModel):
    query_name : str


class QueryCreate(QueryBase):
    pass 

class Query(QueryBase):
    query_id : int 

    class Config:
        orm_mode = True



# class NewsBase(BaseModel):
#     title: str
#     description: str
#     url: str
#     query_name: str
#     publishedAt: datetime
#     storedAt: datetime
#     query_id: int

#     class Config:
#         orm_mode = True
