import tweepy
import pandas as pd
import json
from datetime import datetime


def run_twitter_stream(token):
    # Authenticate to Twitter [more about tweepy: https://docs.tweepy.org/en/stable/]
    auth = tweepy.OAuthHandler(token.access_key, token.access_secret)
    auth.set_access_token(token.consumer_key, token.consumer_secret)

    # Create an API object
    api = tweepy.API(auth)

    # Access the tweets from selected user's timeline
    tweets = api.user_timeline(screen_name="nanashimumei_en",
                               # Not including retweets
                               include_rts=False,
                               count=200,
                               # Necessary to keep full_text
                               # otherwise only the first 140 words are extracted
                               tweet_mode='extended'
                               )

    return tweets
