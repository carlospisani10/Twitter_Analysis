# Dependencies
import tweepy
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Search Term
search_term = input("Which term would you like to search for? ")

# Search for all tweets
public_tweets = api.search(search_term, rpp=5)
# View Search Object
#print(json.dumps(public_tweets, indent=3))

# Loop through all tweets
for tweet in public_tweets["statuses"]:

    # Utilize JSON dumps to generate a pretty-printed json
    #print(json.dumps(tweet, sort_keys=True, indent=4))
    print(tweet["text"])
