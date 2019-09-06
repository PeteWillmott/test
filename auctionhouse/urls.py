"""auctionhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from accounts.urls import index, login, logout, register
from news.urls import news, reviews
from news.models import News, Review
from catalogue.urls import view_all, view_one
from catalogue.models import Catalogue
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^login$', login, name="login"),
    url(r'^logout$', logout, name="logout"),
    url(r'^register$', register, name="register"),
    url(r'^news$', news, name="news"),
    url(r'^reviews$', reviews, name="reviews"),
    url(r'^auctions$', view_all, name="catalogue-all"),
    url(r'^auctions/(?P<id>\d+)/$', view_one, name="catalogue-one"),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
