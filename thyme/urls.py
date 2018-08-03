from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepageSearchQuery/', views.homepageSearchQuery, name='homepageSearchQuery'),    
]