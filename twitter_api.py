# -*- coding: utf-8 -*-
# tweepy文档地址：http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html#hello-tweepy
import tweepy

consumer_key='jWTX99jrzBIWBd8Ezy7QSXyzB'
consumer_secret='hf07wlqaTWwUEDPvqmtFq7qGyv9f70AThfZzF8pbmS5VZFBPtf'
access_token='712666546414297088-O3aBREV90eM1cdeiMv2Afj7IuBLCZSo'
access_token_secret='agvzIG2vL9xVPHas0i1y1HpchKwxyvdtklEboIFuhXO8H'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# 使用代理proxy
api = tweepy.API(auth,proxy='178.34.176.86:8080')

# 获取自己twtter的前20条内容
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
