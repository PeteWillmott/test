from django.test import TestCase

class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get("/login")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_get_registration_page(self):
        page = self.client.get("/register")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")
