from django.shortcuts import render
from .models import News, Review

def news(request):
    articles = News.objects.all()
    return render(request, 'news.html', {"articles": articles})


def reviews(request):
    review = Review.objects.all()
    return render(request, 'reviews.html', {"review": review})

