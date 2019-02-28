# Business.py

# Business name 
# Busines_id 
# business_overall_review (i.e. 4.5total)
# review_count
# overall_sentiment
# reviews = {review_id: sentiment}, 

import Review

class Business:
    def __init__(self, business_dict):
        self.id = business_dict['id']
        self.name = business_dict['name']
        self.review_count = business_dict['review_count']
        self.stars = business_dict['rating']
        self.reviews = '[Review]'
        self.overall_sentiment = 'avg of all sentiments'


    
        