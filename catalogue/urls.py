from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from .views import view_all, view_one
from .models import Catalogue

urlpatterns = [
    url(r'^auctions$', view_all, name="catalogue-all"),
    url(r'^auctions/(?P<id>\d+)/$', view_one, name="catalogue-one")
]