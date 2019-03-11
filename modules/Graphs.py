
import pygal

class Graph:

    def __init__(self, businesses):
        self.businesses = businesses
        self.rating_bar == self.rating_bar()
        self.sentiment_bar = self.sentiment_bar()

    def rating_bar(self):
        line_chart = pygal.HorizontalBar()
        line_chart.title = 'Business Ratings'
        line_chart.x_labels = map(str, range(0, 5))
        for b in self.businesses:
            line_chart.add(b.name, float(b.rating))

    def sentiment_bar(self):
        line_chart = pygal.HorizontalBar()
        line_chart.title = 'Business Sentiment Score'
        line_chart.x_labels = map(str, range(-1, 1))
        for b in self.businesses:
            line_chart.add(b.name, float(b.sentiment_score))

    # @staticmethod
    # def rating_bar(businesses):
    #     line_chart = pygal.HorizontalBar()
    #     line_chart.title = 'Business Sentiment Score'
    #     line_chart.x_labels = map(str, range(-1, 1))
    #     for b in businesses:
    #         line_chart.add(b.name, int(b.sentiment_score))
    #     line_chart.render()
