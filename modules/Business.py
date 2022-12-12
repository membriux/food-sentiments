"""
Business.py
Contains a classes that deal with Businesses:
   - A Business class to represent Business objects
   - A class called GatherBusinesses to hold a list of
     all of the businesses that were retreived
"""

# python built in module for dealing with json objects
import json

# python module for requesting data from sites
import requests

# Class that represents a Review object
from modules.Review import Review

# the API KEY needed for getting data from Yelp
import os

# for testing purposes
import pprint

# Used when retreiving data from Yelp
HEADERS = {'Authorization': 'bearer {}'.format(os.getenv('API_KEY'))}

# A dictionary where the keys are business ids and the values are
# dictionaries of reviews. This dictionary stores
# all reviews for each business. A global dictionary is
# necessary to minimize our calls from Yelp. Yelp has a limit
# on how many API calls we can make per day, so storing the
# data we retreive, to minimize API calls, is ideal
ALL_REVIEWS = {}

# constants
LIMIT = 9
RADIUS = 35000

# pprint for testing purposes
pp = pprint.PrettyPrinter()

class GatherBusinesses:
    """
    This class gets user input
    and retrieves a list of businesses
    from Yelp, based on the input
    """
    def __init__(self, term, location):
        # list of businesses
        self.term = term
        self.location = location
        self.business_list = self._get_businesses()

    # Helper methods which are private and should not be accessed outside
    # of this class:

    def _get_businesses(self):
        """
        Retrieves a list of businesses
        """
        businesses = []
        params = self._get_params_for_search()
        business_dict = self._get_business_data(params)
        for d in business_dict:
            businesses.append(Business(d))
        return businesses

    def _get_params_for_search(self) -> dict:
        """
        get user input for term and location
        """

        return {'term': self.term, 'limit': LIMIT,
        'radius': RADIUS, 'location': self.location}

    def _get_business_data(self, params: dict) -> dict:
        """
        returns data from yelp given search criteria in the form
        of search term (such as 'tacos'), limit of search, radius,
        and location
        """
        endpoint = 'https://api.yelp.com/v3/businesses/search'
        response = requests.get(url = endpoint, params = params, headers = HEADERS)
        data = response.json()['businesses']
        return data

class Business:
    def __init__(self, business_dict):
        # public attributes that can be accessed by
        # other files:

        self.id = business_dict['id']
        self.name = business_dict['name']
        self.review_count = business_dict['review_count']
        self.rating = business_dict['rating']

         # a list of Review objects
        self.reviews = self._get_reviews()

        # Sentiment score is calculated using all of the reviews
        # for this business and get the the feeling based on the score
        self.sentiment_score = self._calculate_sentiment_score()
        self.overall_sentiment = self._get_overall_sentiment()

    # Helper methods which are private and should not be accessed outside
    # of this class:

    def _ensure_json_exists(self):
        """
        Checks if a review.json file exists
        in the directory. If it does not exist,
        this method creates the file.
        """
        try:
            f = open('review.json', 'r')
            f.close()
        except FileNotFoundError:
            f = open('review.json', 'w')
            f.close()

    def _get_reviews(self) -> [Review]:
        """
        Helper function for retrieving reviews data
        from yelp
        Returns a list of Review objects
        """
        global ALL_REVIEWS
        self._ensure_json_exists()
        with open('review.json', 'r') as js:
            try:
                ALL_REVIEWS = json.load(js)
                if self.id in ALL_REVIEWS:
                    return self._get_list_of_reviews()
                else:
                    self._add_more_reviews()
                    return self._get_list_of_reviews()
            except json.decoder.JSONDecodeError:
                self._add_more_reviews()
                return self._get_list_of_reviews()

    def _get_list_of_reviews(self):
        """
        Helper function used for retreiving
        reviews
        """
        global ALL_REVIEWS
        reviews_data = ALL_REVIEWS[self.id]['reviews']
        list_of_reviews = []
        for review_dict in reviews_data:
            list_of_reviews.append(Review(review_dict))
        return list_of_reviews

    def _add_more_reviews(self):
        """
        Adds more reviews to the global
        dictionary
        """
        global ALL_REVIEWS
        with open('review.json', 'w') as j_file:
            endpoint = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(self.id)
            response = requests.get(url = endpoint, headers = HEADERS)
            ALL_REVIEWS[self.id] = response.json()
            json.dump(ALL_REVIEWS, j_file, sort_keys=True, indent=4)

    def _calculate_sentiment_score(self):
        """
        Calculates the sentiment score for this
        business using all of the reviews
        """
        total = 0
        for review in self.reviews:
            total += float(review.sentiment)
        analysis = total/len(self.reviews)
        return "%.2f" % analysis

    def _get_overall_sentiment(self):
        """
        Determine the overall sentiment for this
        business using the sentiment score
        """
        score = float(self.sentiment_score)
        if score < -0.50:
            return 'Negative'
        elif -0.50 <= score < -0.25:
            return 'Somewhat Negative'
        elif -0.25 <= score < 0.25:
            return 'Neutral'
        elif 0.25 <= score < 0.50:
            return 'Somewhat positive'
        elif 0.50 <= score:
            return 'Positive'










print()
