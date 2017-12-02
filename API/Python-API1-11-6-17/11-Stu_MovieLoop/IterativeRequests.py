# Dependencies
import random
import json
import requests

# Let's get the JSON for 100 posts sequentially.
url = "https://opentable.herokuapp.com/api/restaurants/"
response_json = []

# Create a list of OpenTable IDs for some Austin restaurants
rest_id = [3964, 139159, 110398, 152164, 85471, 19090, 17689]

# Loop through our restaurant IDs
for i in rest_id:
    print("Making request for Restaurant ID " + str(i) + ".")

    post_response = requests.get(url + str(i))
    post_response = post_response.json()

    # Save post's JSON
    response_json.append(post_response)

# Now we have 7 objects, which are the results of querying the API per each restaurant ID.
print("We have " + str(len(response_json)) + " restaurants!")

for j in response_json:
    print(j['name'] + ", " + j['address'])
