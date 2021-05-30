import time
import tweepy
from tweepy.api import API


consumer_key = 'fnD17HFfMimWyLs64qEvE3Ido'
consumer_secret = 'v0kSb9AMCbJnEgbN4uF9PPC62koef24ekn4WS9kr68yLzTvKzm'
key = '1213705763304030208-QcNTONDreu7LETVRJPuSmeZnXaKNxU'
secret = 'NPKuprP8jxQkyt2VVSehBnFSSPL2l0n8M2CYYm6RV4OKV'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = "#KejriwalControlsCorona"
tweetnumber = 3 
tweets = tweepy.Cursor(api.search, hashtag ).items(tweetnumber) ; 

def search():
    for tweet in tweets :
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3); 

search()