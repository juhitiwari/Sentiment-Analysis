#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 23:05:16 2018

@author: slytherin
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

ckey="oa7MVRcrPLkWiaJlybuLdNf0X"
csecret="FgyOZo29W47jiW5TAogfiIC0qiUOQ7rVlhpkYqUJezFtqwYZeX"
atoken="998973958367014913-LEJRU3DKjA3KppVbfpeF1LilKwDaZBy"
asecret="wV2B4UhPY5SUt669c0NN1CcbgKKtNSbfQJvUuSR9ON97j"
class listener(StreamListener):

    def on_data(self, data):
        	
        all_data = json.loads(data)
        tweet=all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        
        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["India"])
