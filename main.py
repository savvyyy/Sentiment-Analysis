from flask import Flask
from flask_restful import Api, Resource, reqparse
from sentiment import sentimentAnalysis
from absa import absa

app = Flask(__name__)
api = Api(app)

class SentimentAnalysisResult(Resource):
    def __init__(self):
        pass

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('hashtag', type=str, required=True)
        args = parser.parse_args()

        return sentimentAnalysis('#'+args.hashtag), 200

class AspectSentimentAnalysis(Resource):
    def __init__(self):
        pass

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('hashtag', type=str, required=True)
        args = parser.parse_args()

        return absa('#'+args.hashtag), 200

class IntentSentimentAnalysis(Resource):
    def __init__(self):
        pass

    def get(self):
        pass


api.add_resource(SentimentAnalysisResult, '/getSentiment')
api.add_resource(AspectSentimentAnalysis, '/absa')

if __name__ == "__main__":
    app.run(debug=True)