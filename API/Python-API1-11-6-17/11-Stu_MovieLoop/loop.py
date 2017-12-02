# Dependencies
import random
import json
import requests as req

#get url
url = "http://www.omdbapi.com/?apikey=d93d1d07&t="
json_list = []

# Create a list of Movie names for some the OMDB API
movies = ["Aliens", "Sing", "Moana"]

#run da loop
for x in movies: 
    print(f'I wanna know stuff about {movies}.')

    info_movie = req.get(url + x)
    movie_json = info_movie.json()

    # Save post's JSON
    json_list.append(movie_json)