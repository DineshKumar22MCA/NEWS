# from news_app import fetch_queries
# from news_app import news_api
# import requests
# from datetime import datetime
# from news_app.models import News
# from news_app.database import SessionLocal
# from dateutil import parser

# query_data = fetch_queries.fetch_and_print_queries()

# # print(query_data)
# print(type(query_data))

# # db = SessionLocal()


# for i in query_data :
#     query_id = i["query_id"] 
#     query_name = i["query_name"]
#     print("==============================")
#     print(query_name)

#     articles = news_api.fetch_everything_news(query_name) 
#     # print(articles[:1])

#     for idx, article in enumerate(articles[:5], start=1):
#         title = article.get("title" , "No title Available")
#         description = article.get("description" , "No Description Available")
#         url = article.get("url" , "No URL Available")
#         publishedAt = article.get("publishedAt" , "No data Available")
#         storedAt = datetime.now()

#         if publishedAt != "No data Available":
#             publishedAt = parser.parse(publishedAt)

#         db = SessionLocal()

#         try:
#             news_entry = News(
#                 title = title,
#                 description = description ,
#                 url = url ,
#                 query_name = query_name ,
#                 publishedAt = publishedAt ,
#                 storedAt = storedAt ,
#                 query_id = query_id
#             )
#             db.add(news_entry)
#             db.commit()
#             print(query_name ," news added ")
#         except Exception as e:
#             print(f"Error : {e}")
#             db.rollback()
#         finally:
#             db.close()




#         print("_________________________________")
#         print(f"Title : {title}")
#         print(f"descrption : {description}")
#         print(f"url : {url}")
#         print(f"query_name : {query_name}")
#         print(f"publishedAt : {publishedAt}")
#         print(f"storedAt : {storedAt}")
#         print(f"query_id : {query_id}")

# # do not use  {
#         # news_entry = News(
#         #     title = title,
#         #     description = description,
#         #     url = url ,
#         #     query_name = query_name ,
#         #     publishedAt = publishedAt ,
#         #     storedAt = storedAt ,
#         #     query_id = query_id ,
#         # )

#         # db.add(news_entry)
#         # print("query news added")

#     # db.commit()
#     # print(f"{query_name} : data commited successfully")
# # }


# print("all data inserted successfully")

# # db.close() --dnu



        



import asyncio
import time
# get  news without duplicate

from news_app import fetch_queries
from news_app import news_api
import requests
from datetime import datetime
from news_app.models import News
from app.database import SessionLocal
from dateutil import parser
# from news_app.celery.celery_worker import celery_app

from news_app.celery.celery_app import celery_app


@celery_app.task
def fetch_news_task():
    try:
        query_data = fetch_queries.fetch_and_print_queries()

        for i in query_data:
            query_id = i["query_id"] 
            query_name = i["query_name"]
            # print("==============================")
            # print(query_name)

            articles = news_api.fetch_everything_news(query_name) 
            print(len(articles))
            for idx, article in enumerate(articles[:5], start=1):
                title = article.get("title", "No title Available")
                description = article.get("description", "No Description Available")
                url = article.get("url", "No URL Available")
                publishedAt = article.get("publishedAt", "No data Available")
                storedAt = datetime.now()

                if publishedAt != "No data Available":
                    publishedAt = parser.parse(publishedAt)

                db = SessionLocal()

                try:
                    existing_news = db.query(News).filter(News.title == title).first()
                    # print(f"***************{existing_news}*********************")

                    if existing_news:
                        # print(f"Duplicate news detected: {title}. Skipping.")
                        # news_entry = News(
                        #     title="Dummy Title for Testing",  
                        #     description="This is a dummy description for testing ",  # Dummy description
                        #     url="https://dummyurl.com",  
                        #     publishedAt=datetime.now(),
                        #     storedAt=storedAt,
                        #     query_id=query_id
                        # )
                        # db.add(news_entry)
                        # db.commit()
                        # print("dummy record saved")
                        continue
                    else:
                        news_entry = News(
                            title=title,
                            description=description,
                            url=url,
                            query_name=query_name,
                            publishedAt=publishedAt,
                            storedAt=storedAt,
                            query_id=query_id
                        )
                        db.add(news_entry)
                        db.commit()
                        # print(query_name, "news added")
                except Exception as e: 
                    print(f"Error: {e}")
                    db.rollback()
                finally:
                    db.close()

                    # print("_________________________________")
                    # print(f"Title: {title}")
                    # print(f"Description: {description}")
                    # print(f"URL: {url}")
                    # print(f"Query Name: {query_name}")
                    # print(f"Published At: {publishedAt}")
                    # print(f"Stored At: {storedAt}")
                    # print(f"Query ID: {query_id}")

        # print("All data inserted successfully")
    except Exception as e:
        print(e)




# fetch_news_task()

@celery_app.task 
def callback_post(query_name: str, callback_url: str):
    print("---------------------------------------------------------")
    print(f"start====={query_name}")
    try:
        articles =  news_api.fetch_everything_news(query_name)
        top5 = articles[:5]
        clean_articles = []
        for article in top5:
            clean_articles.append({
                "query_name" :query_name ,
                "title" : article.get("title"),
                "description":article.get("description"),
                "url":article.get("url"),
                "publishedAt":article.get("publishedAt")
            })

        result = {
            "query_name": query_name,
            "news": clean_articles,
            "fetched_at": datetime.utcnow().isoformat()
        }
        time.sleep(15)
        print(f"end ===={query_name}")
        print("------------------------------------------------")
        response = requests.post(callback_url, json=result)
        response.raise_for_status() 
        # return {"status": "success", "callback_response": response.json()}
        return result
    except Exception as e:
        print(f"Error in ask_anything_task: {e}")
        raise e
