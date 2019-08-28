from django.conf.urls import url
from .views import view_all, view_one, item_create

app_name = 'catalogue'
urlpatterns = [
    url(r'^$', view_all, name="view_all"),
    url(r'^add$', item_create, name="item_create"),
    url(r'^(?P<id>\d+)/$', view_one, name="view_one")
]