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
    path('addrecipe/', views.addrecipe, name='addrecipe'),
    path('writerecipe/', views.writerecipe, name='writerecipe'),
    path('homepageSearchQuery/', views.homepageSearchQuery, name='homepageSearchQuery'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('mycontributedthymelines/', views.mycontributedthymelines, name='mycontributedthymelines'),
    path('thymeline/', views.thymeline, name='thymeline'),
]
