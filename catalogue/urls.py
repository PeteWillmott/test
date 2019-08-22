from django.conf.urls import url
from .views import view_all

urlpatterns = [
    url(r'^catalogue/all$', view_all, name="view_all"),
]