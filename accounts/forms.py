from django import forms


class UserLoginForm(forms.Form):
    """Form to be user for user login."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)