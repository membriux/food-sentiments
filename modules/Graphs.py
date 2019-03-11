import pygal

"""
Graph class used to construct three graphs.
It takes in an array of business and constructs
three graphs using the data collected.
"""
class Graph:

    def __init__(self, businesses):
        self.businesses = businesses
        self.rating_bar = self.rating_bar()
        self.sentiment_bar = self.sentiment_bar()
        self.comparison_bar = self.comparison_bar()

    '''
    Construct graph that compares
    businesses and their ratings
    '''
    def rating_bar(self):
        line_chart = pygal.HorizontalBar()
        line_chart.title = 'Business Ratings'
        # line_chart.x_labels = map(str, range(0, 5))
        for b in self.businesses:
            line_chart.add(b.name, float(b.rating))
        chart = line_chart.render_data_uri()
        return chart

    '''
    Construct graph that compares
    businesses and sentiment_scores
    '''
    def sentiment_bar(self):
        line_chart = pygal.HorizontalBar()
        line_chart.title = 'Business Sentiment Score'
        # line_chart.x_labels = map(str, range(-1, 1))
        for b in self.businesses:
            line_chart.add(b.name, float(b.sentiment_score))
        chart = line_chart.render_data_uri()
        return chart

    '''
    Construct graph that shows the difference
    between sentiment_score vs the ratings.
    '''
    def comparison_bar(self):
        line_chart = pygal.Bar()
        line_chart.title = 'Comparison of Ratings vs. Score'
        line_chart.x_labels = map(str, [b.name for b in self.businesses])
        line_chart.add('Sentiment Score', [float(b.sentiment_score)+1 for b in self.businesses])
        line_chart.add('Rating', [float(b.rating)/2.5 for b in self.businesses])
        chart = line_chart.render_data_uri()
        return chart
