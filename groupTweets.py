from datetime import datetime
import os.path
from os import path
import pandas as pd
from functions import getTwitterData, getPolarity

def createGroup(hashTagSubject):
    print('hashTagSubject',hashTagSubject)
    public_tweets_path = os.getcwd() + '/' + hashTagSubject + '.csv'

    if path.exists(public_tweets_path):
        print('hai')
        public_tweets =  pd.read_csv(os.path.realpath(public_tweets_path))
        tweetText = []
        polarity = []
        for i in range(0, len(public_tweets)):
            tweetText.append({
                'tweet' : public_tweets['tweet'][i],
                'date' : public_tweets['created_at'][i]
            })
        sortedTweets = sorted(tweetText,key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S:%f'), reverse=False)

        for tweet in sortedTweets:
            polarity.append({
                'date' : tweet['date'],
                'polarity' : getPolarity(tweet['tweet'])
            })
    
        return polarity

    else:
        print('nai hai')
        public_tweets_file = getTwitterData(hashTagSubject)
        public_tweets_path = public_tweets_file + '/' + hashTagSubject + '.csv'
        public_tweets =  pd.read_csv(os.path.realpath(public_tweets_path))

        tweetText = []
        polarity = []
        for i in range(0, len(public_tweets)):
            tweetText.append({
                'tweet' : public_tweets['tweet'][i],
                'date' : public_tweets['created_at'][i]
            })
        sortedTweets = sorted(tweetText,key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S:%f'), reverse=False)

        for tweet in sortedTweets:
            polarity.append({
                'date' : tweet['date'],
                'polarity' : getPolarity(tweet['tweet'])
            })
    
        return polarity

    








    # print('hashTagSubject', hashTagSubject)
#     public_tweets = getTwitterData(hashTagSubject)
#     tweetText = []
#     polarity = []
#     for tweet in public_tweets:
#         tweetText.append({
#             'date' : tweet.created_at.strftime('%Y-%m-%d %H:%M:%S:%f'),
#             'tweet' : tweet.text,
#             'user' : tweet.user.name
#         })
#     # print('tweetText', tweetText)
#     sortedTweets = sorted(tweetText,key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S:%f'), reverse=False)
    
#     for tweet in sortedTweets:
#         polarity.append({
#             'date' : tweet['date'],
#             'polarity' : getPolarity(tweet['tweet'])
#         })
    
#     return polarity
# createGroup('dog')