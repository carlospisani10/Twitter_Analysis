# Dependencies
import requests as req
import json

# URL for GET requests to retrieve Star Wars character data
url = "https://swapi.co/api/people/"

# Storing the JSON response within a variable
response = req.get(url + '4')
response_json = response.json()


# Collecting the name of the character collected
name = str((response_json["name"]))
print(name)


# Counting how many films the character was in
movies = str((len(response_json["films"])))
print(movies)

# Figure out what their first starship was
url_ship = "https://swapi.co/api/starships/13/"
response_ship =  req.get(url_ship)
ship_json = response_ship.json()
ship_name = str((ship_json["name"]))
print(ship_name)

# Print character name and how many films they were in
print(f'{name} was in {movies} films. Their first ship was the {ship_name}') 

# Print what their first ship was
install citipy