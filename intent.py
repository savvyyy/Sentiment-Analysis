from functions import predictions, get_final_output, load_dataset, getTwitterData

# def intentPrediction(text):
#     filename = './data.csv'
#     intent, unique_intent, sentences = load_dataset(filename)
#     pred = predictions(text)
#     return get_final_output(pred, unique_intent)

def intentPrediction(hashTagSubject):
    filename = './data.csv'
    intent, unique_intent, sentences = load_dataset(filename)
    public_tweets = getTwitterData(hashTagSubject)
    tweetText = []
    prediction = []
    intentData = []
    for tweet in public_tweets:
        tweetText.append(tweet.text)
    for text in tweetText:
        predict = predictions(text)
        prediction.append(predict)
    for pred in prediction:
         intentData.append(get_final_output(pred, unique_intent))
    return intentData