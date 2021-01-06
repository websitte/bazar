#from django import urls
from django.urls import path 
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('zbrane/', views.Zbrane.as_view(), name='zbrane'),

]