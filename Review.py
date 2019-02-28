# Review.py

class Review:
    def __init__(self, review_dict):
        self.review_text = review_dict['text']
        self.sentiment = 0
        self.stars = review_dict['stars']
        self.username = review_dict['user_id']

    def generate_username(self):
        pass

    



