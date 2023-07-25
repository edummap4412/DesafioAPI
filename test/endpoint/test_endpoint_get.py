import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from sdk.get_api import NewsAPISDK


class ArticleListViewIntegrationTest(APITestCase):
    def setUp(self):
        self.url = reverse('article-list')

    def test_list_articles_integration(self):
        sdk = NewsAPISDK()
        articles = sdk.get_articles()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.content)
        self.assertEqual(len(data), len(articles))

        for article_data in data:
            self.assertIn('author', article_data)
            self.assertIn('title', article_data)
            self.assertIn('description', article_data)

