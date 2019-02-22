import nltk
import ssl
from textblob import TextBlob


def get_review_sentiment(review) -> int:
    """
    Analyze sentiment of each review and
    return the integer representing the sentiment
    of that review
    """
    analysis = TextBlob(review)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def get_reviews():
    """
    Get reviews from Yelp API that josh
    is working on
    """
    print()





# INSTALL NLTK PACKAGES
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()