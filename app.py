from flask import Flask
from modules.Business import GatherBusinesses


BUSINESSES = []

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome!'

# Get the info about business
def analyze_businesses():
    global BUSINESSES
    b = GatherBusinesses()
    BUSINESSES = b.business_list
    print('Analyzing businesses\n')
    for b in BUSINESSES:
        print(b.name)
        print(b.review_count)
        print(b.rating)
        print(b.reviews)
        print(b.overall_sentiment)


if __name__ == '__main__':
    print('Running app...')
    analyze_businesses()
    app.run()





