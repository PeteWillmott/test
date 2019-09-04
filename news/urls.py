from django.conf.urls import url
from .views import news, reviews
from .models import News, Review

"""
    Wire up correctly to display as blocks on index
"""

urlpatterns = [
    url(r'^news$', news, name="news"),
    url(r'^reviews$', reviews, name="reviews"),
]