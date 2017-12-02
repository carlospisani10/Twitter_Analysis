import requests
import json

# Note that the ?apikey= is a query param for your api key
url = "http://www.omdbapi.com/?apikey=d93d1d07"

# Who was the director of the movie **Aliens**?
# We're concatenating the t= parameter, which specifies the movie title we're trying to find
title_param1 = "&t=Aliens"
url1 = url + title_param1
response1 = requests.get(url1)
json1 = response1.json()
director = str((json1["Director"]))
print(f'The director of the movie "Aliens" was {director}.')

#What was the movie **Gladiator** rated?
title_param2 = "&t=Gladiator"
url2 = url + title_param2
response2 = requests.get(url2)
json2 = response2.json()
rating= str((json2["Rated"]))
print(f'The rating of the movie Gladiator is {rating}.')

#What year was **50 First Dates** released? 
title_param3 = "&t=50 First Dates"
url3 = url + title_param3
response3 = requests.get(url3)
json3 = response3.json()
date= str((json3["Released"]))
print(f'The movie 50 First Dates was released on {date}.')

#Who wrote Moana
title_param4 = "&i=tt3521164"
url4 = url + title_param4
response4 = requests.get(url4)
json4 = response4.json()
writer= str((json4["Writer"]))
print(f'The movie Moana was written by the following writers: {writer}.')