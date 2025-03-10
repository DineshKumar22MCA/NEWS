
# fastapi
from fastapi import FastAPI , Depends , HTTPException ,Body ,requests
from fastapi import Query , Request
from typing import Optional
from celery.result import AsyncResult
# sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import or_
# fastapi_crud.app
from app import models,schemas,crud,database 
from sqlalchemy import or_
# news_app import files
from news_app.models import News 

from pydantic import BaseModel , Field
from datetime import datetime
from collections import defaultdict
# from .schemas import *
from fastapi.responses import JSONResponse
from news_app.main import *

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()



def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/create_query/",response_model=schemas.Query)
def create_query(query : schemas.QueryCreate , db:Session = Depends(get_db)):
    return crud.create_query(db=db , query=query)


@app.get("/get_all_queries/", response_model=list[schemas.Query])
def read_queries(skip: int=0, limit: int=100, db : Session =Depends(get_db)):
    queries = crud.get_queries(db=db , skip=skip, limit=limit)
    return queries 



@app.get("/get_query_by_id/{query_id}", response_model=schemas.Query)
def read_query(query_id: int , db : Session = Depends(get_db)):
    db_query = crud.get_query(db=db , query_id = query_id)

    if db_query is None:
        raise HTTPException(status_code=404, detail = "query not found")
    return db_query


@app.put("/queries/{query_id}", response_model=schemas.Query)
def update_queries(query_id : int , query : schemas.QueryCreate , db : Session = Depends(get_db)):
    db_query = crud.update_query(db=db, query_id= query_id, query=query)

    if db_query is None:
        raise HTTPException(status_code=404, detail="query not found")
    return db_query



@app.delete("/queries/{query_id}", response_model=schemas.Query)
def delete_query(query_id : int , db :Session =Depends(get_db)):
    db_query = crud.delete_query(db=db , query_id=query_id)

    if db_query is None:
        raise HTTPException(status_code=404, detail="Query not found")
    return db_query 





# news app end points 


class NewsBase(BaseModel):
    news_id : int
    title : str
    description : str = Field(default="No description available") 
    url : str
    query_name : str
    publishedAt : datetime
    storedAt : datetime
    query_id : int

    class Config:
        orm_mode = True




# working endpoint get all news list[{dict}] format
@app.get("/news", response_model= list[NewsBase] )
def get_news(db : Session = Depends(get_db)):
    news_items = db.query(News).all()
    for item in news_items:
        print(item.news_id)
    return news_items 



# getting news dict of list of dict - py script
@app.get("/getting_news_list_dict", response_model=dict[str, list[NewsBase]])
def get_news_listdict(db: Session = Depends(get_db)):
    all_news = db.query(News).all()

    if not all_news:
        raise HTTPException(status_code=404, detail="No news found")
    
    listdict_news = defaultdict(list)
    for i in all_news:
        listdict_news[i.query_name].append(i)

    return dict(listdict_news)



@app.get("/news/{news_id}", response_model=NewsBase)
def get_news_by_id(news_id : int,db : Session = Depends(get_db)):
    news1 = db.query(News).filter(News.news_id == news_id).first()
    if not news1:
        raise HTTPException(status_code=404 , detail="news not available")
    return news1



@app.get("/search_news", response_model=list[NewsBase])
def search_news(search: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(News)

    print(query)
    if search:
        query = query.filter(
            (News.title.ilike(f"%{search}%")) | (News.description.ilike(f"%{search}%"))
        )

    news_items = query.all()
    return news_items




class QueryRequest(BaseModel):
    query_name: str
    callback_url: str


@app.post("/callback_news")
async def callback(data: QueryRequest):
    # await asyncio.sleep(1)
    query_name = data.query_name
    task =  callback_post.delay(query_name)
    print(task)
    return {"task id" : task.id, "query_name":query_name, "task status": task.status}



@app.get("/callback_url_status/{task_id}")
async def callback_status(task_id : str):
    task = AsyncResult(task_id)
    task_status = task.status
    task_state = task.state
    print(task_state,task_status)
    return {"task status :":task_status, "task state : ": task_state }


@app.get("/callback_result/{task_id}")
async def callback_result(task_id: str):
    task_result = AsyncResult(task_id)

    if task_result.state == "PENDING":
        return {"task_id": task_id, "status": "PENDING", "message": "Task is still running"}

    elif task_result.state == "SUCCESS":
        return {"task_id": task_id, "status": "SUCCESS", "result": task_result.result}

    elif task_result.state == "FAILURE":
        return {"task_id": task_id, "status": "FAILURE", "error": str(task_result.result)}

    return {"task_id": task_id, "status": task_result.state}




