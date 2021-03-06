# Dependencies
import json
import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Get all tweets from home feed
public_tweets = api.home_timeline()

# Loop through all tweets
for tweet in public_tweets:
    # Utilize JSON dumps to generate a pretty-printed json
    print(json.dumps(tweet, sort_keys=True, indent=4))
