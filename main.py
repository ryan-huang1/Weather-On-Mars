from keep_alive import keep_alive
import schedule
import datetime
import requests
import random
import tweepy
import json
import time
import os

keep_alive()

#variables for accessing twitter API
consumer_key=os.environ['consumer_key']
consumer_secret_key=os.environ['consumer_secret_key']
access_token=os.environ['access_token']
access_token_secret=os.environ['access_token_secret']

d = datetime.datetime.now()

def main():
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
        weatherUpdate = f'Good morning astronaut! Today’s a {randomPositveWord()} {dayOfTheWeek()} in the Jezero Crater. It\'s currently {funcSeasonData()}, with a high of {funcMaxTempData()} and low of {funcMinTempData()}. Sunrise is at {funcSunriseData()}, sunset is at {funcSunsetData()}. Have a nice day! \U0001F44B'

        f = open("tweets.txt", "a")
        f.write(f'{d} {weatherUpdate}\n\n')
        f.close()

        print('weather tweet posted')
        return(weatherUpdate)

    def noWeatherTweet():
        responses = ["sending data back to Earth", "fueling rockets", "collecting samples", "saving energy for the storm ahead", "greeting new astronauts", "driving around", "scanning Mars's surface", "taking videos of Ingenuity", "hanging out with Curiosity", "texting Zhurong", "taking with mission control", "visiting Opportunity", "talking with my satilite buddies", "finding water", "trying to find new microbial friends", "trying to produce oxygen"]
        activity = random.choice(responses)
        
        tweet = f'Sorry no new update today, I was busy {activity}. Check back tomorrow! \U0001F44B'

        f = open("tweets.txt", "a")
        f.write(f'{d} {tweet}\n\n')
        f.close()

        return(tweet)

    def mainFunction():
        if str(lastdate) == str(date):
            api.update_status(noWeatherTweet())
            print(noWeatherTweet())
            print('no update posted')
        else:
            api.update_status(weatherTweet())
            print(weatherTweet())
            print('weather update posted')

    #post tweet/status
    oauth = OAuth()
    api = tweepy.API(oauth)

    mainFunction()

    f = open("dates.txt", "w")
    f.write(date)
    f.close()

def OAuth():
    auth=tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def retweet_function():

    oauth = OAuth()
    api = tweepy.API(oauth)

    #get latest tweet function
    tweets = api.user_timeline(screen_name="NASAPersevere")
    status = tweets[0]
    print(status.id)
    retweet_id = str(status.id)

    f = open("last_retweet.txt", "r")
    last_retweet = f.readline()[0:19]

    if retweet_id == last_retweet:
        f = open("retweets.txt", "a")
        f.write(f'{d} no new retweet today\n\n')
        f.close()
    else:
        #retweet function
        retweet_response = api.retweet(id=retweet_id)
        print(retweet_response)

        f = open("retweets.txt", "a")
        f.write(f'{d} retweeted:{status.text} tweetID:{retweet_id}\n\n')
        f.close()

        f = open("last_retweet.txt", "w")
        f.write(retweet_id)
        f.close()

schedule.every().day.at("14:00").do(main)
schedule.every(1).hours.do(retweet_function)

while True:
    schedule.run_pending()
    time.sleep(1)