from rest_framework.response import Response
from sdk.get_api import NewsAPISDK
from rest_framework import generics


class ArticleListView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        sdk = NewsAPISDK()
        articles = sdk.get_articles()
        article_list = []

        for article in articles:
            author = article.get('author', 'Unknown Author')
            title = article.get('title', 'No Title')
            description = article.get('description', 'No Description')
            article_list.append({
                'author': author,
                'title': title,
                'description': description
            })

        return Response(article_list)
