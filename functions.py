import re
import en_core_web_sm
import tweepy
import os
from textblob import TextBlob
from dotenv import load_dotenv
load_dotenv()

def getTwitterData(hashTagSubject):
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    public_tweets = api.search(hashTagSubject,count=100)

    return public_tweets

def getPolarity(text):
    textAnalysis = TextBlob(text)
    polarity = textAnalysis.sentiment.polarity
    # subjectivity = textAnalysis.sentiment.subjectivity
    return polarity

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+|@[^\s]+')
    return url_pattern.sub(r'', text)

def sentimentData(data):
    if data['Polarity'] >= 0.05:
        val = "Positive"
    elif data['Polarity'] <= -0.05:
        val = "Negative"
    else:
        val = "Neutral"
    return val

def getAspect(text):
    nlp = en_core_web_sm.load()
    doc = nlp(text)
    aspects = [token.text for token in doc if token.pos_ == "NOUN"]
    return aspects