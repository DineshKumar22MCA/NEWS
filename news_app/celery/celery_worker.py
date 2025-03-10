# from eventlet import monkey_patch
# monkey_patch()

# from celery import Celery
# # from news_app.main import fetch_news_task

# celery_app = Celery('news_app' , broker='redis://localhost:6379/0')

# celery_app.conf.timezone = 'UTC'

# celery_app.conf.beat_schedule = {
#     'fetch_news_every_5_minutes' : {
#         'task' : 'news_app.main.fetch_news_task' ,
#         'schedule' : 30.0 
#     },
# }

from . import celery_app  
from news_app.main import fetch_news_task 

if __name__ == '__main__':
    celery_app.start()

