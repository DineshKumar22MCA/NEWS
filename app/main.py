
# app import files
from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
from app import models,schemas,crud,database 
from typing import Optional
from sqlalchemy import or_
from fastapi import Query

# news_app import files
from news_app.models import News 
from pydantic import BaseModel
from datetime import datetime

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()



def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/queries/",response_model=schemas.Query)
def create_query(query : schemas.QueryCreate , db:Session = Depends(get_db)):
    return crud.create_query(db=db , query=query)


@app.get("/queries/", response_model=list[schemas.Query])
def read_queries(skip: int=0, limit: int=100, db : Session =Depends(get_db)):
    queries = crud.get_queries(db=db , skip=skip, limit=limit)
    return queries



@app.get("/queries/{query_id}", response_model=schemas.Query)
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
    description : str
    url : str
    query_name : str
    publishedAt : datetime
    storedAt : datetime
    query_id : int

    class Config:
        orm_mode = True



@app.get("/news", response_model= list[NewsBase] )
def get_news(db : Session = Depends(get_db)):
    news_items = db.query(News).all()
    for item in news_items:
        print(item.news_id)
    return news_items




@app.get("/news/{news_id}", response_model=NewsBase)
def get_news_by_id(news_id : int,db : Session = Depends(get_db)):
    news1 = db.query(News).filter(News.news_id == news_id).first()
    if not news1:
        raise HTTPException(status_code=404 , detail="news not available")
    return news1




# working endpoint1
# @app.get("/search_news", response_model=list[NewsBase])
# def search_news(title: Optional[str] = None , description: Optional[str] = None, db: Session = Depends(get_db),):
#     query = db.query(News)
    
#     if title:
#         query = query.filter(News.title.ilike(f"%{title}%"))
#     if description:
#         query = query.filter(News.description.ilike(f"%{description}%"))
    
#     news_items = query.all()
#     return news_items







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





# not working endpoint
# @app.get("/search_news",response_class=list[NewsBase])
# def search_news(title : Optional[str]=None, description:Optional[str]=None, db:Session=Depends(get_db)):
#     query = db.query(News)

#     if title or description:
#         query = query.filter(News.title.ilike(f"%{title or description}%"))
    
    
#     news_items = query.all()
#     return news_items