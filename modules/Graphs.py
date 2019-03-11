
import pygal

class Graph:

    def __init__(self, businesses):
        self.businesses = businesses
        self.rating_bar = self.rating_bar()
        self.sentiment_bar = self.sentiment_bar()

    def rating_bar(self):
        line_chart = pygal.HorizontalBar()
        line_chart.title = 'Business Ratings'
        # line_chart.x_labels = map(str, range(0, 5))
        for b in self.businesses:
            line_chart.add(b.name, float(b.rating))
        chart = line_chart.render_data_uri()
        return chart

    def sentiment_bar(self):
        line_chart = pygal.HorizontalBar()
        line_chart.title = 'Business Sentiment Score'
        # line_chart.x_labels = map(str, range(-1, 1))
        for b in self.businesses:
            line_chart.add(b.name, float(b.sentiment_score))
        chart = line_chart.render_data_uri()
        return chart

    def comparison_bar(businesses):
        line_chart = pygal.Bar()
        line_chart.title = 'Comparison of Ratings vs. Score'
        line_chart.x_labels = map(str, range(-1, 1))
        for b in businesses:
            line_chart.add(b.name, int(b.sentiment_score))
        line_chart.render()
