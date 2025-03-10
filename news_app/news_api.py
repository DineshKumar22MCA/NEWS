import requests
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__),"../env/.search")
load_dotenv(dotenv_path)

GNEWS_API_KEY=os.getenv("GNEWS_API_KEY")
NEWSAPI_API_KEY=os.getenv("NEWSAPI_API_KEY")

GNEWS_BASE_URL=os.getenv("GNEWS_BASE_URL")
NEWSAPI_BASE_URL=os.getenv("NEWSAPI_BASE_URL")


def fetch_everything_news(query_name):
    language ="en"
    sort_by = "publishedAt"

    params = {
        "q" : query_name,
        "lang" : language,
        "sortby": sort_by,
        "token" : GNEWS_API_KEY
    }
    params2 = {
        "q": query_name,
        "language": language,
        "sortBy": sort_by,
        "apiKey": NEWSAPI_API_KEY
    }
    
    response = requests.get(GNEWS_BASE_URL,params=params)
    # response = requests.get(NEWSAPI_BASE_URL,params=params2)
    data = response.json()
    
    if response.status_code==200:
        return data.get("articles",[])
    else:
        print(f"Error fetching news : {data.get('message','unknown error')}")
        return []
    



def display_news(articles):
    if not articles:
        return "No news articles found."
    
    for idx, article in enumerate(articles[:1], start=1):
        title = article.get("title", "No title available")
        description = article.get("description", "No description available")
        url = article.get("url", "No URL available")
        published_at = article.get("publishedAt", "No publish date available")
        
        print(f"{idx}. Title: {title}")
        print("--------------------------------")
        print(f"Description: {description}")
        print("--------------------------------")
        print(f"Published at: {published_at}")
        print("--------------------------------")
        print(f"URL: {url}\n")



# articles = fetch_everything_news("aus")
# display_news(articles)









