# Dependencies
import tweepy
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User
target_user = "GuardianData"

# Tweet Texts
tweet_texts = []

# Create a loop to iteratively run API requests
for x in range(10):

    # Get all tweets from home feed (for each page specified)
    public_tweets = api.user_timeline(target_user, page=x)

    # Loop through all tweets
    for tweet in public_tweets:

        # Print Tweet
        print(tweet["text"])

        # Store Tweet in Array
        tweet_texts.append(tweet["text"])

# Print the Tweet Count
print("Tweet Count: " + str(len(tweet_texts)))
