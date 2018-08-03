from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('createnew/', views.createnew, name='createnew'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('namethymeline/', views.namethymeline, name='namethymeline'),
    path('homepageSearchQuery/', views.homepageSearchQuery, name='homepageSearchQuery'),
]