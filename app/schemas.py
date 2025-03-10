
from pydantic import BaseModel
# from datetime import datetime
from pydantic import BaseModel, HttpUrl

class QueryBase(BaseModel):
    query_name : str


class QueryCreate(QueryBase):
    pass 

class Query(QueryBase):
    query_id : int 

    # class Config:
    #     orm_mode = True




# class CallbackRequest(BaseModel):
#     query_name: str
#     callback_url: HttpUrl
    

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
