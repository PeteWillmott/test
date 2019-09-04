from django.shortcuts import render
from .models import News, Review

def news(request):
    article = News.objects.last()
    return render(request, 'lead_news_item.html', {"article": article})


def reviews(request):
    review = Review.objects.all()
    return render(request, 'reviews.html', {"review": review})

