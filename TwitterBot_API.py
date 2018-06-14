import tweepy
import sched, time
import datetime
from threading import Timer

class TwitterNews():

    def __init__(self,access_token,access_secret,consumer_token,consumer_secret):
        #predefined OAuth parameters
        self.auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
        self.auth.set_access_token(access_token,access_secret)
        self.api = tweepy.API(self.auth)
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def retrieveTimeline(self):
        #retrieve timeline
        public_tweets = self.api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)

    def tweetNow(self,message):
        #sends a tweet request with a message
        self.api.update_status(message)

    def scheduleTweet(self,timer,message):
        #Schedules a tweet with a delay
        Timer(timer,self.tweetNow,(message)).start()
