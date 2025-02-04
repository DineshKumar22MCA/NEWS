from sqlalchemy import Column ,Integer , String ,DateTime ,ForeignKey,ForeignKeyConstraint
from sqlalchemy.sql import func
from datetime import datetime
from app.database import engine, Base
from app.models import Query
# from .database import Base

class News(Base):
    __tablename__ = "news"

    news_id = Column(Integer , primary_key=True, index=True)
    title  = Column(String(500))
    description = Column(String(1000))
    url = Column(String(255))
    query_name = Column(String(255))
    publishedAt = Column(DateTime,nullable=True)
    storedAt = Column (DateTime , default=func.now())
    query_id = Column (Integer , ForeignKey(Query.query_id, ondelete="CASCADE"), nullable =False)


    # query_id = Column(Integer, nullable=False)
    # __table_args__ = (
    #     ForeignKeyConstraint(
    #         ['query_id'], ['queries.query_id'],
    #         ondelete='CASCADE'
    #     ),
    # )

    # query_id = Column(Integer, nullable=False)
    # __table_args__ = (
    #     ForeignKeyConstraint(
    #         ['query_id'], ['mydb.queries.query_id'],
    #           ondelete='CASCADE'
    #     ),
    # )



Base.metadata.create_all(bind=engine)




# sqlalchemy.exc.NoReferencedTableError:
# Foreign key associated with column 'news.query_id' 
# could not find table 'mydb.queries' with which to generate 
# a foreign key to target column 'query_id'