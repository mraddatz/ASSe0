from django.db import models


class NewsArticle:

    def __init__(self, news):
        self.source = news['source']['name']
        self.author = news['author']
        self.title = news['title']
        self.description = news['description']
        self.url = news['url']
        self.urlToImage = news['urlToImage'] if news['urlToImage'] else "https://media.istockphoto.com/illustrations/news-lettering-drawing-illustration-id165927838"
        self.publishedAt = news['publishedAt']
        self.content = news['content']


# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=300)
    alias = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')