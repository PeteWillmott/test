from django.test import TestCase

class TestDisplayViews(TestCase):

    def test_news_view(self):
        page = self.client.get("/news")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "news.html")

    def test_review_view(self):
        page = self.client.get("/reviews")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "reviews.html")