from django.shortcuts import render
from catalogue.models import Catalogue
from news.models import News

def index(request):
    """Return the index.html file."""
    newest_picture = Catalogue.objects.exclude(sale_status=True).last()
    top_two_blogs = News.objects.all()[:2]
    context = {
        "newest_picture": newest_picture,
        "top_two_blogs": top_two_blogs
    }
    return render(request, 'index.html', context)


def about(request):
    """Background info on the company."""
    return render(request, 'about.html')


def contact(request):
    """Contact details for the company."""
    return render(request, 'contact.html')


def faq(request):
    """General information about the company and the website."""
    return render(request, 'faq.html')


def how_to(request):
    """Instructions onhow to use the bidding function."""
    return render(request, 'how-to.html')


def shipping(request):
    """Customer advice on shipping."""
    return render(request, 'shipping.html')

