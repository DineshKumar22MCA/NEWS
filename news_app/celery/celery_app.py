

from celery import Celery

celery_app = Celery('news_app', broker='redis://localhost:6379/0')
celery_app.autodiscover_tasks(packages=["news_app"],related_name="main")
celery_app.conf.timezone = 'UTC'


# from news_app.main import fetch_news_task

celery_app.conf.beat_schedule = {
    'fetch_news_every_5_minutes': {
        'task': 'news_app.main.fetch_news_task', 
        'schedule': 5.0, 
    },
}
