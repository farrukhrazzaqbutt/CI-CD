from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include 
from djangoApp.views import *

urlpatterns = [
    path('', home, name='home'),
]
