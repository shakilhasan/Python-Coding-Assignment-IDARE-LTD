from django.conf.urls import url
from . import  views
from django.urls import path




urlpatterns = [
    path('', views.home, name='home'),
    path('result', views.result, name='result'),

 ]
