import ansa

ansa_service = ansa.Ansa()

feed = ansa_service.getNews(ansa.constants.HOMEPAGE[1])
print(feed)
