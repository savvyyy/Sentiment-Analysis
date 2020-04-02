from functions import predictions, get_final_output, load_dataset, getTwitterData

def intentPrediction(hashTagSubject):
    filename = './data.csv'
    intent, unique_intent, sentences = load_dataset(filename)
    public_tweets = getTwitterData(hashTagSubject)
    tweetText = []
    prediction = []
    final_data = []
    for tweet in public_tweets:
        tweetText.append(tweet.text)
    for text in tweetText:
        predict = predictions(text)
        prediction.append(predict)
    for pred in prediction:
         final_data.append(get_final_output(pred, unique_intent))
    # print('final_data', final_data)
    intentData = []
    for i in range(len(tweetText)):
        intentData.append({
            'tweet' : tweetText[i],
            'intent' : final_data[i]
        })
    return intentData