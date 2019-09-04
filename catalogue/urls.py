from django.conf.urls import url
from .views import view_all, view_one, item_create, item_update

app_name = 'catalogue'
urlpatterns = [
    url(r'^$', view_all, name="view_all"),
    url(r'^add$', item_create, name="item_create"),
    url(r'^update/(?P<id>\d+)/$', item_update, name="item_update"),
    url(r'^(?P<id>\d+)/$', view_one, name="view_one")
]