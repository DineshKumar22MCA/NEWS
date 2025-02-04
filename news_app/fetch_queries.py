import requests


BASE_URL = "http://127.0.0.1:8000/get_all_queries"


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

