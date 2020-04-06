import pandas as pd
import datetime, csv, os, json
import os.path
from os import path

from functions import remove_urls, sentimentData, getAspect, getPolarity, getTwitterData

def absa(hashTagSubject):
    print('hashTagSubject', hashTagSubject)
    public_tweets_path = os.getcwd() + '/' + hashTagSubject + '.csv'
    if path.exists(public_tweets_path):
        print('hai')
        
        data = pd.read_csv(os.path.realpath(public_tweets_path))
        data["tweet"] = data["tweet"].astype(str)
        data["tweetclean"] = data["tweet"].apply(lambda text: remove_urls(text))
        data["Polarity"] = data["tweet"].apply(getPolarity)
        data['Sentiment'] = data.apply(sentimentData, axis=1)
        data["Aspects"] = data["tweet"].apply(getAspect)
        

        aspect_list = data.to_dict(orient='records')
        return aspect_list

    else:
        print('nai hai')
        public_tweets_file = getTwitterData(hashTagSubject)
        public_tweets_path = public_tweets_file + '/' + hashTagSubject + '.csv'
        # public_tweets =  pd.read_csv(os.path.realpath(public_tweets_path))

        data = pd.read_csv(os.path.realpath(public_tweets_path))
        data["tweet"] = data["tweet"].astype(str)
        data["tweetclean"] = data["tweet"].apply(lambda text: remove_urls(text))
        data["Polarity"] = data["tweet"].apply(getPolarity)
        data['Sentiment'] = data.apply(sentimentData, axis=1)
        data["Aspects"] = data["tweet"].apply(getAspect)
        

        aspect_list = data.to_dict(orient='records')
        return aspect_list
        # tweetText = []
        # for tweet in public_tweets['tweet']:
        #     tweetText.append(tweet.text)

    # filename = hashTagSubject + str(datetime.datetime.now()) + '.csv'


    # with open(filename, 'w',newline="") as file_writer:
    #     fields=["id","tweet"]
    #     writer=csv.DictWriter(file_writer,fieldnames=fields)
    #     writer.writeheader()
    #     for i in range(0, len(tweetText)):
    #         writer.writerow({"id": i,"tweet": tweetText[i]})

    # data = pd.read_csv(os.path.realpath(filename))

    
    # data["tweet"] = data["tweet"].astype(str)
    # data["tweetclean"] = data["tweet"].apply(lambda text: remove_urls(text))
    # data["Polarity"] = data["tweet"].apply(getPolarity)
    # data['Sentiment'] = data.apply(sentimentData, axis=1)
    # data["Aspects"] = data["tweet"].apply(getAspect)

    # # print('dataaa',data)
    # aspect_list = data.to_dict(orient='records')
    # # print('data', data)
    # # for index, rows in data.iterrows():
    # #     row_list = [rows.text, rows.Polarity, rows.Sentiment, rows.Aspects]
    # #     aspect_list.append(row_list)
    # return aspect_list