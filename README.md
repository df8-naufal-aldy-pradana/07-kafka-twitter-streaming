# 07-kafka-twitter-streaming

This is a simple example of how to use Kafka to stream tweets from Twitter's API.

## How to run

1. Clone the repository
```bash
git clone https://github.com/df8-naufal-aldy-pradana/07-kafka-twitter-streaming.git
```

2. Change the twitter credential used for auth on src/twitter_credentials.py, you can get it from [here](https://developer.twitter.com/en/apps)

3. You can also change the twitter_stream.py func to fit your needs better, you can find the documentation [here](https://developer.twitter.com/en/docs/tweets/filter-realtime/api-reference/post-statuses-filter)

4. Run docker-compose
```bash
docker-compose up
```
