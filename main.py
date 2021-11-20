import requests
import tweepy
import json
import os

#variables for accessing twitter API
consumer_key=os.environ['consumer_key']
consumer_secret_key=os.environ['consumer_secret_key']
access_token=os.environ['access_token']
access_token_secret=os.environ['access_token_secret']

def OAuth():
    auth=tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return auth

#func to parse data
def funcWeatherJSON():
    weather = requests.get("https://mars.nasa.gov/rss/api/?feed=weather&category=mars2020&feedtype=json")
    # processes the raw data into JSON
    weatherJSON = json.loads(weather.text)
    return(weatherJSON)

def funcDateData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['terrestrial_date']
    return(tempatureData)

def funcSolData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['sol']
    return(tempatureData)

def funcSeasonData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['season']
    return(tempatureData)

def funcMinTempData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['min_temp']
    return(tempatureData)

def funcMaxTempData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['max_temp']
    return(tempatureData)

def funcPressureData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['pressure']
    return(tempatureData)

def funcSunriseData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['sunrise']
    return(tempatureData)

def funcSunsetData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['sunset']
    return(tempatureData)


#post tweet/status
oauth = OAuth()
api = tweepy.API(oauth)

api.update_status('well there buddy hello testing')
print('tweet posted')

