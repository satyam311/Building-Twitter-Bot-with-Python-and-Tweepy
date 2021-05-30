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



FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id 

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME , 'w')
    file_write.write(str(last_seen_id))
    file_write.close(); 
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode ='extended')
    for tweet in reversed(tweets): 
        if '#randomtweet' in tweet.full_text.lower():
            print("New Tweet  found") 
            print(str(tweet.id) + ' - ' + tweet.full_text) 
            api.update_status("@" + tweet.user.screen_name + " Good I will help you " , tweet.id) 
            api.create_favorite(tweet.id)

            api.retweet(tweet.id)

            store_last_seen(FILE_NAME, tweet.id)
    
while True: 
    reply()
    time.sleep(60)


