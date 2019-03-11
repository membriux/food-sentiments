from flask import Flask, url_for, render_template, request, session
from modules.Business import GatherBusinesses, Business
from modules.Graphs import Graph
import json
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

BUSINESSES = []
SEARCH = {'term': None, 'location': None}
GRAPHS = None


@app.before_request
def setup():
    global BUSINESSES, SEARCH
    if 'user' not in session:
        SEARCH = {}


@app.route('/', methods=['GET', 'POST'])
def index():
    # Store session of user
    session['user'] = os.urandom(8)

    if request.method == 'POST' and \
            request.form['term'] != '' and \
            request.form['location'] != '':

        # Get search inputs
        SEARCH['term'] = request.form['term']
        SEARCH['location'] = request.form['location']
        # Get businesses
        analyze_businesses()


    if BUSINESSES != [] and SEARCH != {}:
        return render_template('index.html', search=True,
                                businesses=BUSINESSES,
                                schart=GRAPHS.sentiment_bar.render_data_uri(),
                                rchart=GRAPHS.rating_bar.render_data_uri(),
                                location=SEARCH['location'], term=SEARCH['term'])
    else:
        return render_template('index.html')


@app.route('/reviews/<bid>')
def business(bid):
    print('\n\nBusinesses:', BUSINESSES)
    for b in BUSINESSES:
        if bid == b.id:
            return render_template('routing/business.html',
                                    business=b)

# Get the info about business
def analyze_businesses():
    global BUSINESSES
    term, location = SEARCH['term'], SEARCH['location']
    b = GatherBusinesses(term, location)
    BUSINESSES = b.business_list
    get_graphs()


def get_graphs():
    global GRAPHS
    GRAPHS = Graph(BUSINESSES)


if __name__ == '__main__':
    app.run(debug=True)
