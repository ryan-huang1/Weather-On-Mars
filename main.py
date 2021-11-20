import os
import tweepy

#variables for accessing twitter API
consumer_key=os.environ['consumer_key']
consumer_secret_key=os.environ['consumer_secret_key']
access_token=os.environ['access_token']
access_token_secret=os.environ['access_token_secret']

def OAuth():

    try:
        auth=tweepy.OAuthHandler(consumer_key, consumer_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()
api = tweepy.API(oauth)

api.update_status('well there buddy')
print('tweet posted')
