"""
Review.py
Contains a class that represents a Review object.
"""

from textblob import TextBlob

class Review:
    def __init__(self, review_dict):
        # public attributes that can be accessed by
        # other files:

        self.text = review_dict['text']
        self.sentiment = self._get_review_sentiment(self.text)
        self.rating = review_dict['rating']
        self.username = review_dict['user']['name']

    def _get_review_sentiment(self, review) -> int:
        """
        Analyze sentiment of each review and
        return the integer representing the sentiment
        of that review
        """
        analysis = TextBlob(review)
        return '%.2f' % analysis.sentiment.polarity
