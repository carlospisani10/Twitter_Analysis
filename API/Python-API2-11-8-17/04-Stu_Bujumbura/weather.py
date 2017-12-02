# Dependencies
import requests as req
import json

#save info
api_key = "15383539ac6ad7827e835523385021b3"
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "Bujumbura"
units = "metric"

#build query URL
query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

#Get weather response
weather_response = req.get(query_url)
json=weather_response.json()

#
temp = json["main"]["temp"]

#print(json)
print(f'The weather api came up with {temp} celcius.')