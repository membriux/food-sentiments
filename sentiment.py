import nltk
import ssl
from textblob import TextBlob
from collections import defaultdict
import requests
import pprint
# create a py file called YelpAPI and put your API key there:
from YelpAPI import API_KEY


pp = pprint.PrettyPrinter()
HEADERS = {'Authorization': 'bearer {}'.format(API_KEY)}

def get_review_sentiment(review) -> int:
    """
    Analyze sentiment of each review and
    return the integer representing the sentiment
    of that review
    """
    
    analysis = TextBlob(review)
    return analysis.sentiment.polarity

