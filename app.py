from flask import Flask, url_for, render_template, request
from modules.Business import GatherBusinesses, Business
import json

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


@app.route('/reviews/<bid>')
def business(bid):
    for b in BUSINESSES:
        if bid == b.id:
            return render_template('routing/business.html',
                                    business=b)

# Get the info about business
def analyze_businesses(term, location):
    global BUSINESSES
    b = GatherBusinesses(term, location)
    BUSINESSES = b.business_list


if __name__ == '__main__':
    print('Running app...')
    app.run()
