from flask import Flask, url_for, render_template, request, session
from modules.Business import GatherBusinesses, Business
from modules.Graphs import Graph
import pygal
import json
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

BUSINESSES = []
SEARCH = {'term': None, 'location': None}
GRAPHS = None

"""
Before each request from the web,
we check if the user is in session so that
it gets it's personal unique search.
"""
@app.before_request
def setup():
    global BUSINESSES, SEARCH
    if 'user' not in session:
        SEARCH = {}


"""
Main page. It returns a page with two fields
that the user must give input (food term and location).
Once the user submits a search the program returns
all the results about the search
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    # Store session of user
    session['user'] = 'user'

    if request.method == 'POST' and \
            request.form['term'] != '' and \
            request.form['location'] != '':

        # Get search inputs
        SEARCH['term'] = request.form['term']
        SEARCH['location'] = request.form['location']
        # Get businesses
        analyze_businesses()


    if BUSINESSES != [] and SEARCH != {}:
        top = get_top()
        return render_template('index.html', search=True,
                                topsent=top[0],
                                toprating=top[1],
                                businesses=BUSINESSES,
                                rchart=GRAPHS.rating_bar,
                                schart=GRAPHS.sentiment_bar,
                                srchart=GRAPHS.comparison_bar,
                                location=SEARCH['location'], term=SEARCH['term'])
    else:
        return render_template('index.html')


"""
View specific reviews made by customers
along with the rating and the sentiment_score
that was calculated.
"""
@app.route('/reviews/<bid>')
def business(bid):
    print('\n\nBusinesses:', BUSINESSES)
    for b in BUSINESSES:
        if bid == b.id:
            return render_template('routing/business.html',
                                    business=b)
"""
About Page
"""
@app.route('/about')
def about():
    return render_template('about.html')


"""
Get businesses from Yelp API and create
graphs using the data collected.
"""
def analyze_businesses():
    global BUSINESSES
    term, location = SEARCH['term'], SEARCH['location']
    b = GatherBusinesses(term, location)
    BUSINESSES = b.business_list
    get_graphs()

"""
Get the top business based on ratings
and the top business based on sentiment_score.
"""
def get_top():
    tops, topr = None, None
    s, r = 0, 0
    for b in BUSINESSES:
        if float(b.sentiment_score) > s:
            s = float(b.sentiment_score)
            tops = b
        if float(b.rating) > r:
            r = float(b.rating)
            topr = b
    return [tops, topr]

"""
Use the Graph class to construct the three
graphs: sentiment_score graph, rating graph,
and the comparsion graph.
"""
def get_graphs():
    global GRAPHS
    GRAPHS = Graph(BUSINESSES)


if __name__ == '__main__':
    app.run(debug=True)
