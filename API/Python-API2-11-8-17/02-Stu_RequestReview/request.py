# Dependencies
import requests as req
import json

# URL for GET requests to retrieve Star Wars character data
url = "http://nyt-mongo-scraper.herokuapp.com/api/headlines"

# Storing the JSON response within a variable
response = req.get(url)
json = response.json()

first = json[0]
last = json[-1]
number = len(json)


print(last)
print(first)
print(number)