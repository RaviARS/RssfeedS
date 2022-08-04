from django.contrib import admin
from django.urls import path, include
from .views import home, category, publish

urlpatterns = [
    path('', home, name='home'),
    path('category', category, name='category'),
    path('publish', publish, name='publish'),

]
