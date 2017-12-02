# Dependencies
import requests as req

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
api_key = "194b3fc29096414a94a1361bb983fb3b"

# Search for articles that mention granola
q = "granola"

# Build query URL
query = url + "api-key=" + api_key + "&q=" + q

# Populate articles
articles = req.get(query).json()

# The "response" property in articles contains the actual articles
articles_list = [article for article in articles["response"]["docs"]]

print("Your Reading List:")
for article in articles_list:
    print(article["web_url"])
