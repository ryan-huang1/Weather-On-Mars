import datetime
import requests
import random
import tweepy
import json
import os

#variables for accessing twitter API
consumer_key=os.environ['consumer_key']
consumer_secret_key=os.environ['consumer_secret_key']
access_token=os.environ['access_token']
access_token_secret=os.environ['access_token_secret']

d = datetime.datetime.now()

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

def funcSunriseData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['sunrise']
    return(tempatureData)

def funcSunsetData():
    weatherJSON = funcWeatherJSON()
    tempatureData = weatherJSON['sols'][6]['sunset']
    return(tempatureData)

def randomPositveWord():
    words = ["great", "beautiful", "amazing", "excellent", "marvelous", "superb", "wonderful", "awesome", "incredible", "stunning", "majestic", "magnificent", "awe-inspiring", "spectacular", "fabulous", "dazzling"]
    positive_word = random.choice(words)
    return(positive_word)

def dayOfTheWeek():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayNumber = d.weekday()
    return(days[dayNumber])

date = funcDateData()[8:10]

f = open("dates.txt", "r")
lastdate = f.readline()[0:2]

def weatherTweet():
    weatherUpdate = f'Good morning fellow astronaut! Today’s a {randomPositveWord()} {dayOfTheWeek()} in the Jezero Crater. It\'s currently {funcSeasonData()}, with a high of {funcMaxTempData()} and low of {funcMinTempData()}. Sunrise is at {funcSunriseData()}, sunset is at {funcSunsetData()}. Have a nice day! \U0001F44B'

    f = open("tweets.txt", "a")
    f.write(f'{d} {weatherUpdate}\n\n')
    f.close()
    
    print('weather tweet posted')
    return(weatherUpdate)

if str(lastdate) == str(date):
    print(weatherTweet())
else:
    print('false')

#post tweet/status
oauth = OAuth()
api = tweepy.API(oauth)

#api.update_status('testing testing')
#print('tweet posted')

f = open("dates.txt", "w")
f.write(date)
f.close()

