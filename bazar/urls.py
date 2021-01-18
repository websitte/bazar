#from django import urls
from django.urls import path 
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('novy-inzerat/', views.inz_new, name='inz_new'),
    path('moje-inzeraty/', views.inz_user, name='inz_user'),
    path('detail/<int:pk>/', views.inz_detail, name='inz_detail'),
    path('edit-inzerat/<int:pk>/', views.inz_edit, name='inz_edit'),

]