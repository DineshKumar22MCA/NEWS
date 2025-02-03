# import requests

# API_KEY = "cd2fb428a8a245d5957a6f9086c66a86"  
# BASE_URL = "https://newsapi.org/v2/everything"

# def fetch_everything_news(query="technology", language="en", sort_by="relevancy"):

#     global params
#     params = {
#         "q": query,
#         "language": language,
#         "sortBy": sort_by,
#         "apiKey": API_KEY
#     }

#     response = requests.get(BASE_URL, params=params)
#     data = response.json()

#     if response.status_code == 200:
#         return data.get("articles", {})
#     else:
#         print(f"Error fetching news: {data.get('message', 'Unknown error')}")
#         return []

# def display_news(articles):
#     if not articles:
#         print("No news articles found.")
#         return  "No news articles found."

#     print("\nTop News Articles:\n")
#     # print(articles[1])
#     # print(type(articles))
    
#     for idx, article in enumerate(articles[:2], start=1):
#         print(params["q"])
#         print(f"{idx}. {article['title']} - {article['source']['name']}")
#         print(f"Published at: {article['publishedAt']}")
#         print(f"URL: {article['url']}\n")

#     # idx = 1
#     # for article in articles[:11]:
#     #     print(f"{idx}. {article['title']} - {article['source']['name']}")
#     #     idx += 1


# # if __name__ == "__main__":
# search_query = input("Enter search keyword (default: 'technology'): ") or "technology"
# language = input("Enter language (default: 'en'): ") or "en"
# sort_by = input("Enter sorting preference (relevancy/popularity/publishedAt, default: 'relevancy'): ") or "relevancy"

# articles = fetch_everything_news(search_query, language, sort_by)
# display_news(articles)








import requests

API_KEY = "cd2fb428a8a245d5957a6f9086c66a86"  
BASE_URL = "https://newsapi.org/v2/everything"



def fetch_everything_news(query_name):
    language="en"
    sort_by="relevancy"
    global params
    params = {
        "q": query_name,
        "language": language,
        "sortBy": sort_by,
        "apiKey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        return data.get("articles", [])
    else:
        print(f"Error fetching news: {data.get('message', 'Unknown error')}")
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
        
        # here i should code for insert the news table records using sqlachemy commands

        print(f"{idx}. Title: {title}")
        print("--------------------------------")
        print(f"Description: {description}")
        print("--------------------------------")
        print(f"Published at: {published_at}")
        print("--------------------------------")
        print(f"URL: {url}\n")


# search_query = input("Enter search keyword (default: 'technology'): ") or "technology"
# language = input("Enter language (default: 'en'): ") or "en"
# sort_by = input("Enter sorting preference (relevancy/popularity/publishedAt, default: 'relevancy'): ") or "relevancy"

# articles = fetch_everything_news("aus")
# display_news(articles)














[{'source': {'id': 'wired', 'name': 'Wired'}, 'author': 'Julian Chokkattu', 'title': 'OnePlus 13 and OnePlus 13R Review: Fast and Smooth', 'description': 'The OnePlus 13 sets the stage for a feisty battle between flagship Android smartphones in 2025.', 'url': 'https://www.wired.com/review/oneplus-13-and-oneplus-13r/', 'urlToImage': 'https://media.wired.com/photos/67803b07fbba9a21af074121/191:100/w_1280,c_limit/OnePlus-13-black-and-OnePlus-13R-white-Reviewer-Collage-012025-SOURCE-Julian-Chokkattu.jpg', 'publishedAt': '2025-01-14T16:51:45Z', 'content': "I've been using the OnePlus 13 and OnePlus 13R for the past monththrough the 2024 holiday season and CES 2025which means I've put them through some of the lightest and busiest workloads. There's not … [+3110 chars]"}]