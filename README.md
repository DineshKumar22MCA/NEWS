# News Gathering Application

## Description
This is a FastAPI Server for the project News Gathering Application

## setup

### environment
- Install `python 3.10`, `pip`, and `virtualenv`
- Ensure that present working directory is `News Gathering Application`.
- Create a virtual environment and install the requirements.
```shell
python3.10 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Configuration

#### database
- Use `env/.mock-db` to create `env/.db` to configure the server database connection.
  - Refer `app/database.py`.

#### search
- Use `env/.mock-search` to create `env/.search` to configure the News API keys.
  - Refer `news_app/news_api.py`.

#### Server
- Use `env/.mock-redis` to create `env/.redis` to configure the redis server.
  - Refer `news_app/celery/celery_app.py`.


## Endpoints
- `/`: Not Found
- `/docs`: Swagger UI for the API.
- `/query`: Query for used to manipulating the queries.
    - `POST` : Create a new query in the Query table.
    - `GET` : Retrieve all queries from the Query table.
    - `GET` : `/query/{query_id}` Retrieve a specific query by its query_id.
    - `PUT` : `/query/{query_id}` Update the query name for the given query_id.
    - `DELETE` : `/query/{query_id}` Delete the query from the table.
- `/news` :  `GET` method , Retrieve all news as json format.
- `/news_list` : `GET` method , Retrieve all news as grouped by query_name.
- `/news/{news_id}` : `GET` method, Retrieve a specific news by its news_id.
- `/search_news?=search="keys"` : `GET` method, Retrieve the news by searching keys.
- `callback_news` : `POST` method,Send the query to Background process. If we post the query_name and callback_url ,it will return the task_id.
- `/callback_url_status/{task_id}` : `GET` method, Retrieve  task status for given task_id.
- `/callback_result/{task_id}` : `GET` method, Retrieve  task result for given task_id.


## Usage
- Execute the script.

```shell
uvicorn app.main:app --reload
```
- The server is running on `http://127.0.0.1:8000`. Change the IP address if necessary.
- The server can be stopped by pressing `Ctrl + C`.

```shell
sudo service redis-server start
```
- To check the redis server in shell ```redis-cli ping```
- To stop the redis server in shell ```sudo service redis-server stop```

```shell
python -m celery -A news_app.celery.celery_app worker --pool=solo -l info
```
- We can change the celery pool(prefork, threads, gevent, eventlet) if we want.
- The server can be stopped by pressing `Ctrl + C`.

```shell
python -m celery -A news_app.celery.celery_app beat --loglevel=info
```
- Celery beat trigger the event five minutes once.
- The server can be stopped by pressing `Ctrl + C`.
