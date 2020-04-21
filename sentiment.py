import csv
import datetime
import os.path
from os import path
import pandas as pd
from functions import calculatePolarity, getTwitterData

# cwd = os.getcwd()
# print(cwd)

def sentimentAnalysis(hashTagSubject):
    print('hashTagSubject',hashTagSubject)
    public_tweets_path = os.getcwd() + '/' + hashTagSubject + '.csv'
    if path.exists(public_tweets_path):
        print('hai')
        public_tweets =  pd.read_csv(os.path.realpath(public_tweets_path))
        polarity= []
        totalCount = 0
        tweetText = []
        for tweet in public_tweets['tweet_without_url']:
            totalCount = totalCount+1
            tweetText.append(tweet)
            data = calculatePolarity(tweet)
            polarity.append(data)

        if(totalCount > 0):
            Sum = sum(polarity)
            average = Sum/len(polarity)
            if(average > 0 and average < 0.5):
                # print("happy")
                return {
                    'average': average,
                    'sentiment': 'positive'
                }
            elif(average > 0.5 and average <= 1):
                # print("very happy")
                return {
                    'average': average,
                    'sentiment': 'very positive'
                }
            elif(average == 0 or average == 0.0):
                # print("Neutral")
                return {
                    'average': average,
                    'sentiment': 'Neutral'
                }
            elif(average < 0 and average > -0.5):
                # print('Negative')
                return {
                    'average': average,
                    'sentiment': 'Negative'
                }
            elif(average < -0.5 and average > -1):
                # print('Very Negative')
                return {
                    'average': average,
                    'sentiment': 'Very Negative'
                }
        
        else:
            print("No Result Found")
            return {
                'result': 'No Result Found'
            }
    else:
        print('nai hai')
        public_tweets_file = getTwitterData(hashTagSubject)
        public_tweets_path = public_tweets_file + '/' + hashTagSubject + '.csv'
        public_tweets =  pd.read_csv(os.path.realpath(public_tweets_path))
        polarity= []
        totalCount = 0
        tweetText = []
        for tweet in public_tweets['tweet_without_url']:
            totalCount = totalCount+1
            tweetText.append(tweet)
            data = calculatePolarity(tweet)
            polarity.append(data)
    

        if(totalCount > 0):
            Sum = sum(polarity)
            average = Sum/len(polarity)
            if(average > 0 and average < 0.5):
                # print("happy")
                return {
                    'average': average,
                    'sentiment': 'positive'
                }
            elif(average > 0.5 and average <= 1):
                # print("very happy")
                return {
                    'average': average,
                    'sentiment': 'very positive'
                }
            elif(average == 0 or average == 0.0):
                # print("Neutral")
                return {
                    'average': average,
                    'sentiment': 'Neutral'
                }
            elif(average < 0 and average > -0.5):
                # print('Negative')
                return {
                    'average': average,
                    'sentiment': 'Negative'
                }
            elif(average < -0.5 and average > -1):
                # print('Very Negative')
                return {
                    'average': average,
                    'sentiment': 'Very Negative'
                }
        
        else:
            print("No Result Found")
            return {
                'result': 'No Result Found'
            }