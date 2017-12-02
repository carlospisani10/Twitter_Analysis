import requests
import json

# Note that the ?apikey= is a query param for your api key
url = "http://www.omdbapi.com/?apikey=d999c41d"

# Can concatenate different query parameters together (as per API documentation) using '&'
# We're concatenating the t= parameter, which specifies the movie title we're trying to find
title_param = "&t=Aliens"
url = url + title_param

# Performing a GET request, passing in apikey and movie title parameter
response = requests.get(url)

# Converting the response to JSON, and printing the result.
json = response.json()
print(json)

# Print a few keys from the response JSON.
print("Movie was directed by " + json["Director"])
print("Movie was released in " + json["Country"])
