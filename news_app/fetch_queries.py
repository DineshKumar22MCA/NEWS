# import requests


# BASE_URL = "http://127.0.0.1:8000/get_all_queries"
import os
import requests

FASTAPI_HOST = os.getenv("FASTAPI_HOST", "127.0.0.1")
FASTAPI_PORT = os.getenv("FASTAPI_PORT", "8000")


BASE_URL = f"http://{FASTAPI_HOST}:{FASTAPI_PORT}/get_all_queries"


def fetch_and_print_queries():
    try:
        response = requests.get(BASE_URL)

        if response.status_code==200:
            queries = response.json()
            if not queries:
                print("no queries founded in db")
                return None
            else:
                for query in queries:
                    print(query["query_id"])
                    print(query["query_name"])
                return queries
        else:
            print("error occured while fetching queries ")
            return None
    except Exception as e:
        print(f"Error occured While Fetching Queries : {e}")


# fetch_and_print_queries()

