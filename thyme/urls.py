from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('selectthymeline/', views.selectthymeline, name='selectthymeline'),
    path('searchresults/<dishName>/', views.searchresults, name='searchresults'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('createthymeline/', views.createthymeline, name='createthymeline'),
    path('addtimepoint/<dishName>/', views.addtimepoint, name='addtimepoint'),
    path('addtimepoint/', views.addtimepoint, name='addtimepoint'),
    path('writerecipe/', views.writerecipe, name='writerecipe'),
    path('profile/', views.profile, name='profile'),
    path('mycontributedthymelines/', views.mycontributedthymelines, name='mycontributedthymelines'),
    path('thymeline/<thymelineId>/', views.thymeline, name='thymeline'),
    path('family/', views.family, name='family'),
    path('viewrecipe/', views.viewrecipe, name='viewrecipe'),
]

