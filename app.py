from flask import Flask
from Analyzer import get_businesses


BUSINESSES = []

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome!'


# Get the info about business
def analyze_businesses():
    global BUSINESSES
    BUSINESSES = get_businesses()
    print('Analyzing businesses\n')
    for b in BUSINESSES:
        print(b.name)
        print(b.review_count)
        print(b.stars)
        print(b.reviews)
        print(b.overall_sentiment)


if __name__ == '__main__':
    print('Running app...')
    analyze_businesses()
    app.run()





