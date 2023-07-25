import unittest
from sdk.get_api import NewsAPISDK


class TestNewsAPISDK(unittest.TestCase):
    def setUp(self):
        self.sdk = NewsAPISDK()

    def test_get_articles(self):
        articles = self.sdk.get_articles()
        self.assertTrue(isinstance(articles, list), "Articles should be a list")
        for article in articles:
            self.assertIn('author', article, "Article should have 'author' key")
            self.assertIn('title', article, "Article should have 'title' key")
            self.assertIn('description', article, "Article should have 'description' key")