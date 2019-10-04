from django.shortcuts import render
from .models import News, Review

def news(request):
    """Returns blog posts to browse."""
    articles = News.objects.all()
    return render(request, 'news.html', {"articles": articles})


def reviews(request):
    """Returns reviews to browse."""
    review = Review.objects.all()
    return render(request, 'reviews.html', {"review": review})

