import requests
from decouple import config


class NewsAPISDK:
    def __init__(self):
        self.api_url = config('NEWS_API_URL',
                              default='https://newsapi.org/v2/everything?q=tesla&from=2023-06-25&sortBy=publishedAt&apiKey=e680d95a5c55401c9c453df7ecf4a6f6')

    def get_articles(self):
        response = requests.get(self.api_url)
        data = response.json()
        articles = data.get('articles', [])
        return articles

