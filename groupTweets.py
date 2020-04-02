from functions import getTwitterData, getPolarity
from datetime import datetime

def createGroup(hashTagSubject):
    print('hashTagSubject', hashTagSubject)
    public_tweets = getTwitterData(hashTagSubject)
    tweetText = []
    polarity = []
    for tweet in public_tweets:
        tweetText.append({
            'date' : tweet.created_at.strftime('%Y-%m-%d %H:%M:%S:%f'),
            'tweet' : tweet.text,
            'user' : tweet.user.name
        })
    # print('tweetText', tweetText)
    sortedTweets = sorted(tweetText,key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S:%f'), reverse=False)
    
    for tweet in sortedTweets:
        polarity.append({
            'date' : tweet['date'],
            'polarity' : getPolarity(tweet['tweet'])
        })
    
    return polarity
# createGroup('dog')