# from eventlet import monkey_patch
# monkey_patch()

from celery import Celery
import os 

# $env:REDIS_BROKER_URL = "redis://localhost:6379/0" -pwsl
# set REDIS_BROKER_URL=redis://localhost:6379/0 -cmd



broker_url = os.getenv("REDIS_BROKER_URL","redis://localhost:6379/0")

# celery_app = Celery('news_app', broker='redis://redis:6379/0')
celery_app = Celery("news_tasks", broker=broker_url, backend=broker_url, broker_connection_retry_on_startup=True)


celery_app.autodiscover_tasks(packages=["news_app"],related_name="main")
celery_app.conf.timezone = 'UTC'


# from news_app.main import fetch_news_task

celery_app.conf.beat_schedule = {
    'fetch_news_every_5_minutes': {
        'task': 'news_app.main.fetch_news_task', 
        'schedule': 60.0, 
    },
}
