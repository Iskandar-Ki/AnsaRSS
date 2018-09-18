import feedparser

class Ansa():
        
    def __init__(self, *args, **kwargs):
        self.parsed_feed = []

    def getNews(self, xmlrequest):
        feed = feedparser.parse(xmlrequest)
        for item in feed.entries:
            self.parsed_feed.append(self.parseData(item))
        return self.parsed_feed

    def parseData(self, data):
        title = data['title']
        description = data['summary']
        link = data['link']
        pub_date = data['published']
        parsed_data = {
            'title' : title,
            'description' : description,
            'link' : link,
            'pub_date' : pub_date
        }
        return parsed_data