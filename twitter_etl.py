import tweepy
import pandas as pd
import json
from datetime import datetime

def run_twitter_etl():
    
    # Twitter API credentials
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAAf1jwEAAAAAQBido%2BDdSaG63Juo%2Ba0%2FxhV%2BHLE%3D1iiyYrgEWNdrufvoZ6JujZnVtGSk3PNWQvuXvD3Da5qEOIHHMA"
    access_key = "U8dxRixLB4hnsmK6ETUIuyj6o"
    access_secret = "q0wCMs8CeK2QDFbTgwHPjSSGYrkfYmQm2glJqK4c0aMZejIMgc"
    consumer_key = "432387030-IFGBvr1ICNDPJLcKd9JUnOlnjtXErwTASOcIFuJI"
    consumer_secret = "H9FaUWWADbDmGpK6XNe8xd6CHufkV1aE76nZEKWgBvCZJ"

    # Authenticate to Twitter [more about tweepy: https://docs.tweepy.org/en/stable/]
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)
    # client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_key, access_token_secret=access_secret)

    # Create an API object
    api = tweepy.API(auth)

    # Access the tweets from user's timeline
    tweets = api.user_timeline(screen_name="nanashimumei_en", 
                            # 200 is the maximum allowed count     
                            count=200,
                            # Not including retweets
                            include_rts = False,
                            # Necessary to keep full_text
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
    
    return tweets

    # # Create a dataframe from the tweets
    # tweet_list = []
    # for tweet in tweets:
    #     text = tweet._json["full_text"]

    #     refined_tweet = {"user": tweet.user.screen_name,
    #                     "text": text,
    #                     "favorite_count": tweet.favorite_count,
    #                     "retweet_count": tweet.retweet_count,
    #                     "created_at": tweet.created_at,}
    #     # with open("tweet.json", "w") as f:
    #     #     json.dump(refined_tweet, f)
    #     tweet_list.append(refined_tweet)
        
    # # Create a dataframe from the tweets, and save it as a csv file    
    # df = pd.DataFrame(tweet_list)
    
run_twitter_etl()