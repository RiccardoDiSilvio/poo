from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^hi/$', CartForm),
    url(r'^cart/$', CartCreation)
]