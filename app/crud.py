
from sqlalchemy.orm import Session
from app import models, schemas


def create_query(db:Session , query : schemas.QueryCreate):
    db_query = models.Query(query_name = query.query_name)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query 


def get_queries(db:Session , skip : int ,limit : int =100):
    return db.query(models.Query).offset(skip).limit(limit).all()


def get_query(db:Session , query_id : int):
    return db.query(models.Query).filter(models.Query.query_id == query_id).first()


def update_query(db:Session , query_id : int , query : schemas.QueryCreate):
    db_query = db.query(models.Query).filter(models.Query.query_id == query_id).first()

    if db_query:
        db_query.query_name = query.query_name
        db.commit()
        db.refresh(db_query)
        return db_query
    
def delete_query(db:Session , query_id : int):
    db_query = db.query(models.Query).filter(models.Query.query_id == query_id).first()
    temp = db_query 

    if db_query:
        db.delete(db_query)
        db.commit()
        # db.refresh(db_query)
        return temp
    return None



