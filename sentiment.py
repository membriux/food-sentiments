import nltk
import ssl
from textblob import TextBlob
from collections import defaultdict
import requests
# create a py file called YelpAPI and put your API key there:
from YelpAPI import API_KEY

HEADERS = {'Authorization': 'bearer {}'.format(API_KEY)}

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

def get_search_criteria() -> tuple:
    """
    get user input, just default values for now
    """
    return ('tacos', 50, 10000, 'Irvine')

def get_params_for_search() -> dict:
    """
    gets search criteria and returns a dictionary
    representing search parameters
    """
    term, limit, radius, location = get_search_criteria()
    return {'term': term, 'limit': limit, 
    'radius': radius, 'location': location}

def get_business_data() -> dict:
    """
    returns data from yelp given search criteria in the form
    of search term (such as 'tacos'), limit of search, radius, 
    and location
    """
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    params = get_params_for_search()
    response = requests.get(url = endpoint, params = params, headers = HEADERS)
    data = response.json()['businesses']
    return data

def get_reviews_data_from_yelp(business: str):
    """
    Helper function for retrieving reviews data
    from yelp
    """
    endpoint = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business['id'])
    response = requests.get(url = endpoint, headers = HEADERS)
    data = response.json()
    return data['reviews']

def get_reviews() -> {'business name': [('review', 'rating')]}:
    """
    Get reviews from Yelp API
    Right now, it just prints the name of the business followed
    by the review
    """
    search_data = get_business_data()
    count = 2 # just doing 2 businesses for testing but we can get more
    review_data = defaultdict(list)
    for business in search_data:
        if count > 0:
            reviews = get_reviews_data_from_yelp(business)
            for review in reviews:
                review_data[business['name']].append((review['text'], review['rating']))
        else:
            break

        count -= 1

    return dict(review_data)
        
def print_review_sentiments():
    """
    gets reviews and prints them along with the rating 
    and sentiment
    """
    data = get_reviews()
    for name, list_of_reviews in data.items():
        for text, rating in list_of_reviews:
            print(name, ":", text, "RATING:", rating)
            print("SENTIMENT: ", get_review_sentiment(text))
            print('\n\nNEXT REVIEW\n\n')

print_review_sentiments()




# INSTALL NLTK PACKAGES
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()