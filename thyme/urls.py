from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('homepageSearchQuery/', views.homepageSearchQuery, name='homepageSearchQuery'),
]