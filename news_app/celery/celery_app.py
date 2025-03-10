# from eventlet import monkey_patch
# monkey_patch()

from celery import Celery
from dotenv import load_dotenv
import os 

# $env:REDIS_BROKER_URL = "redis://localhost:6379/0" -pwsl
# set REDIS_BROKER_URL=redis://localhost:6379/0 -cmd


dotenv_path = os.path.join(os.path.dirname(__file__), "../env/.redis")
load_dotenv(dotenv_path)

REDIS_BROKER_URL = os.getenv("REDIS_BROKER_URL","redis://localhost:6379/0")

celery_app = Celery("news_tasks", broker=REDIS_BROKER_URL, backend=REDIS_BROKER_URL, broker_connection_retry_on_startup=True)


celery_app.autodiscover_tasks(packages=["news_app"],related_name="main")
celery_app.conf.timezone = 'UTC'


# from news_app.main import fetch_news_task

celery_app.conf.beat_schedule = {
    'fetch_news_every_5_minutes': {
        'task': 'news_app.main.fetch_news_task', 
        'schedule': 60.0, 
    },
}
