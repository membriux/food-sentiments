# Business.py

# Business name 
# Busines_id 
# business_overall_review (i.e. 4.5total)
# review_count
# overall_sentiment
# reviews = {review_id: sentiment}, 

import Review
import json
import pandas
from YelpAPI import API_KEY
import requests


HEADERS = {'Authorization': 'bearer {}'.format(API_KEY)}
REVIEWS = {}


class Business:
    def __init__(self, business_dict):
        self.id = business_dict['id']
        self.name = business_dict['name']
        self.review_count = business_dict['review_count']
        self.stars = business_dict['rating']
        self.reviews = self.get_reviews()
        self.overall_sentiment = 'avg of all sentiments'

    def get_reviews(self):
        """
        Helper function for retrieving reviews data
        from yelp
        """
        global REVIEWS
        with open('review.json', 'r') as js:
            REVIEWS = json.load(js)
            if self.id in REVIEWS:
                return REVIEWS[self.id]

        
        with open('review.json', 'w') as j_file:
            endpoint = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(self.id)
            response = requests.get(url = endpoint, headers = HEADERS)
            data = response.json()
            REVIEWS[self.id] = data
            json.dump(REVIEWS, j_file, sort_keys=True, indent=4)
            
            return REVIEWS[self.id]
    


    
        