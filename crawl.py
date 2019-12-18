############Khoironi2 https://github.com/khoironi2
############source from https://gist.github.com/vickyqian/f70e9ab3910c7c290d9d715491cde44c
import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'uzQrJ1qZT0ShmIENwCr0F2pML'
consumer_secret = 'xhYHr7jfvCDThVjWUxnDkmVNCVxcyCHdyDnHrQyPd5gxkKnKUx'
access_token = '1150637746488107010-fuY42PUlEOVv2TsAIVo5jLCF4ZqoyZ'
access_token_secret = '2gFHEeKh3zZg9BeVXAZG6kfkJCDsZpg0nX9gkCTOGV3NB'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('#bumn.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#bumn",count=2000,
                           lang="id",
                           since="2019-12-16").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])