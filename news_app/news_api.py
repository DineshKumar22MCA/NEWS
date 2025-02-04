# import requests

# API_KEY = "cd2fb428a8a245d5957a6f9086c66a86"  
# BASE_URL = "https://newsapi.org/v2/everything"



# def fetch_everything_news(query_name):
#     language="en"
#     sort_by="publishedAt"   # Options: relevance,relevancy ,publishedAt ,popularity
#     global params
#     params = {
#         "q": query_name,
#         "language": language,
#         "sortBy": sort_by,
#         "apiKey": API_KEY
#     }

#     response = requests.get(BASE_URL, params=params)
#     data = response.json()

#     if response.status_code == 200:
#         return data.get("articles", [])
#     else:
#         print(f"Error fetching news: {data.get('message', 'Unknown error')}")
#         return []

# def display_news(articles):
#     if not articles:
#         print("No news articles found.")
#         return "No news articles found."

#     print("\nTop News Articles:\n")
    
#     for idx, article in enumerate(articles[:1], start=1):
#         title = article.get("title", "No title available")
#         description = article.get("description", "No description available")
#         url = article.get("url", "No URL available")
#         published_at = article.get("publishedAt", "No publish date available")
        

#         print(f"{idx}. Title: {title}")
#         print("--------------------------------")
#         print(f"Description: {description}")
#         print("--------------------------------")
#         print(f"Published at: {published_at}")
#         print("--------------------------------")
#         print(f"URL: {url}\n")


# # search_query = input("Enter search keyword (default: 'technology'): ") or "technology"
# # language = input("Enter language (default: 'en'): ") or "en"
# # sort_by = input("Enter sorting preference (relevancy/popularity/publishedAt, default: 'relevancy'): ") or "relevancy"

# # articles = fetch_everything_news("aus")
# # display_news(articles)





import requests

API_KEY = "290978ff3a40fb0311d7263133c607a0"
BASE_URL = "https://gnews.io/api/v4/search"

# API_KEY2 = "cd2fb428a8a245d5957a6f9086c66a86"
# BASE_URL2 = "https://newsapi.org/v2/everything"


def fetch_everything_news(query_name):
    language ="en"
    sort_by = "publishedAt"

    params = {
        "q" : query_name,
        "lang" : language,
        "sortby": sort_by,
        "token" : API_KEY
    }

    response = requests.get(BASE_URL,params=params)
    data = response.json()

    if response.status_code==200:
        return data.get("articles",[])
    else:
        print(f"Error fetching news : {data.get('message','unknown error')}")
        return []
    



def display_news(articles):
    if not articles:
        print("No news articles found.")
        return "No news articles found."

    print("\nTop News Articles:\n")
    
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









