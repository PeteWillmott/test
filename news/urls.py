from django.urls import path
from .views import news, reviews
from .models import News, Review

app_name = 'news'
urlpatterns = [
    path('news', news, name="news"),
    path('reviews', reviews, name="reviews"),
]