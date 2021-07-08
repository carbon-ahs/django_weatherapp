#created by shehanuk
#url.py of lookup app

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about')
]
