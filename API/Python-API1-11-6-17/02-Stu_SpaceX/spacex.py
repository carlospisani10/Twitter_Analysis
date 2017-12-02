import requests as req
import json

#url for get requests
url_launch = "https://api.spacexdata.com/v1/launches/upcoming"

#send response
response = req.get(url_launch)

#print the response object to the consol
print(response)

#Convert response object to JSON
response = response.json()
response

#Format the print
print(json.dumps(response, indent=4, sort_keys=True))

#print for a specific location
response = req.get(url_launch + "?year=2017")
