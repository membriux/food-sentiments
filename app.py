from flask import Flask, url_for, render_template, request
from modules.Business import GatherBusinesses


BUSINESSES = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and \
            request.form['term'] != '' and \
            request.form['location'] != '':
        # Get search inputs
        term = request.form['term']
        location = request.form['location']
        # Get businesses
        analyze_businesses(term, location)
        # Show results
        return render_template('index.html', search=True,
                                businesses=BUSINESSES,
                                location=location, term=term)
    else:
        return render_template('index.html')

# Get the info about business
def analyze_businesses(term, location):
    global BUSINESSES
    b = GatherBusinesses(term, location)
    BUSINESSES = b.business_list
    # print('Analyzing businesses\n')
    # for b in BUSINESSES:
    #     print(b.name)
    #     print(b.review_count)
    #     print(b.rating)
    #     print(b.sentiment_score)
    #     print(b.overall_sentiment)

if __name__ == '__main__':
    print('Running app...')
    app.run(debug=True)
