from confluent_kafka import Producer
import json
import time
import logging
from src.twitter_stream import run_twitter_stream
import src.twitter_credentials as token
import pandas as pd

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

####################
p = Producer({'bootstrap.servers': 'localhost:9092'})
print('Kafka Producer has been initiated...')
#####################


def receipt(err, msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(
            msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

#####################


def main():
    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at,
        }
        m = json.dumps(refined_tweet, indent=4, sort_keys=True, default=str)
        p.poll(1)
        p.produce('twitter-tracker', m.encode('utf-8'), callback=receipt)
        p.flush()
        tweet_list.append(refined_tweet)

        time.sleep(1)

    # Also save tweets on csv file
    df = pd.DataFrame(tweet_list)
    df.to_csv('result/mumei_tweets.csv')


if __name__ == '__main__':
    tweets = run_twitter_stream(token)
    main()
