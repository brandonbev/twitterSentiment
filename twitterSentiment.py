#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 00:16:10 2020

@author: BrandonVermeer
"""

import twitter

# initialize api instance
twitter_api = twitter.Api(consumer_key='dMK3ktNoQ4ct14czyDyrGtLpf',
                        consumer_secret='88vBB15Trs7kbKGQkrOwc7ZpNoZKgSfcL4Zj0F3pe6qrNZ7hPP',
                        access_token_key='608365061-moXfo9C6Fg9xx8FZfRysydA3QCnzUh20bAZTVBmV',
                        access_token_secret='n3suRC5IuvnC8YVr4yMUHHExZvy224HANk7xXUngIZCXv')

# test authentication
print(twitter_api.VerifyCredentials())

#create test set
def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count = 100)
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None

search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)

print(testDataSet[0:4])

#create training set
import csv
import time
# ""
# #define method for building training set
# def buildTrainingSet(corpusFile, tweetDataFile):
    
#     corpus = []
    
#     with open(corpusFile,'r') as csvfile:
#         lineReader = csv.reader(csvfile,delimiter=',', quotechar="\"")
#         for row in lineReader:
#             corpus.append({"tweet_id":row[2], "label":row[1], "topic":row[0]})
    
#     rate_limit = 180
#     sleep_time = 900/rate_limit
    
#     trainingDataSet = []
    
#     for tweet in corpus:
#         try:
#             status = twitter_api.GetStatus(tweet["tweet_id"])
#             print("Tweet fetched" + status.text)
#             tweet["text"] = status.text
#             trainingDataSet.append(tweet)
#             time.sleep(sleep_time) 
#         except: 
#             continue
#     # now we write them to the empty CSV file
#     with open(tweetDataFile,'w') as csvfile:
#         linewriter = csv.writer(csvfile,delimiter=',',quotechar="\"")
#         for tweet in trainingDataSet:
#             try:
#                 linewriter.writerow([tweet["tweet_id"], tweet["text"], tweet["label"], tweet["topic"]])
#             except Exception as e:
#                 print(e)
#     return trainingDataSet
# ""
#define file paths for input and outputs
corpusFile = "/Users/BrandonVermeer/Desktop/python/corpus.csv"
tweetDataFile = "/Users/BrandonVermeer/Desktop/python/tweetDataFile.csv"

#use buildTrainingSet method to collect training data
trainingData = buildTrainingSet(corpusFile, tweetDataFile)

import re
from nltk.tokenize import word_tokenize
from string import punctuation 
from nltk.corpus import stopwords 




