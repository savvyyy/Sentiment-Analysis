import pandas as pd
import datetime, csv, os, json

from functions import remove_urls, sentimentData, getAspect, getPolarity, getTwitterData

def absa(hashTagSubject):
    public_tweets = getTwitterData(hashTagSubject)
    tweetText = []
    for tweet in public_tweets:
        tweetText.append(tweet.text)

    filename = hashTagSubject + str(datetime.datetime.now()) + '.csv'


    with open(filename, 'w',newline="") as file_writer:
        fields=["id","tweet"]
        writer=csv.DictWriter(file_writer,fieldnames=fields)
        writer.writeheader()
        for i in range(0, len(tweetText)):
            writer.writerow({"id": i,"tweet": tweetText[i]})

    data = pd.read_csv(os.path.realpath(filename))

    
    data["tweet"] = data["tweet"].astype(str)
    data["tweetclean"] = data["tweet"].apply(lambda text: remove_urls(text))
    data["Polarity"] = data["tweet"].apply(getPolarity)
    data['Sentiment'] = data.apply(sentimentData, axis=1)
    data["Aspects"] = data["tweet"].apply(getAspect)

    # print('dataaa',data)
    aspect_list = data.to_dict(orient='records')
    # print('data', data)
    # for index, rows in data.iterrows():
    #     row_list = [rows.text, rows.Polarity, rows.Sentiment, rows.Aspects]
    #     aspect_list.append(row_list)
    return aspect_list