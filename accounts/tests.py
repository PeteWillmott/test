from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get("/login")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_get_registration_page(self):
        page = self.client.get("/register")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")

class TestLoginForm(TestCase):

    def test_log_in(self):
        form = UserLoginForm(
            {"username": "test", "password": "dorwssap"})
        self.assertTrue(form.is_valid())

    def test_error_message(self):
        form = UserLoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["username"], [u"This field is required."])


class TestRegistrationForm(TestCase):

    def test_registration(self):
        form = UserRegistrationForm(
            {"first_name": "George", "last_name": "Washington",
                "username": "Gwash", "email": "GW@email.net",
                "password1": "drowssap4321", "password2": "drowssap4321"})
        self.assertTrue(form.is_valid())

    def test_passwords_do_not_match(self):
        form = UserRegistrationForm(
            {"first_name": "first", "last_name": "last",
                "username": "unique", "email": "test@email.net",
                "password1": "drowssap", "password2": "drowkap"})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], [u"Passwords must match"])
