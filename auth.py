import tweepy
from keys import api_key, api_secret, access_token, access_token_secret, bearer_token

def get_twitter_connection_v1() -> tweepy.API:
    auth = tweepy.OAuth1UserHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True) 
    return api

def get_twitter_connection_v2() -> tweepy.Client:
    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret, wait_on_rate_limit=True)
    return client