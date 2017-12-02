import requests as req
import json

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
api_key = "7e0cbe3353ec484395d9b5b826c35962"

# Search for articles that mention climbing
q = "bouldering"

# Build query URL
query = url + "api-key=" + api_key + "&q=" + q

# Populate articles
articles = req.get(query).json()

# The "response" property in articles contains the actual articles
articles_list = [article for article in articles["response"]["docs"]]

print(articles_list)