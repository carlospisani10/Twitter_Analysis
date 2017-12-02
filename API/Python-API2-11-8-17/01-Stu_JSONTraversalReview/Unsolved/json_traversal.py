# Dependencies
import json

# Load JSON
video_file = open('../Resources/youtube_response.json')
video_json = json.load(video_file)

#
data = video_json["data"]
data_items = data["items"]
title = data_items[0]["title"]

default_thumbnail = data_items[0]["thumbnail"]


print