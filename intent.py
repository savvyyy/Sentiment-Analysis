from functions import predictions, get_final_output, load_dataset

def intentPrediction(text):
    filename = './data.csv'
    intent, unique_intent, sentences = load_dataset(filename)
    pred = predictions(text)
    return get_final_output(pred, unique_intent)