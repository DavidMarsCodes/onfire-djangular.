from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import TemplateView
from .views import login, register, logout, index
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'registro', register, name="register"),
    url(r'login/', login, name="login"),
    url(r'logout/', logout, name="logout"),
   
]