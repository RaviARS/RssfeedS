from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'home/home.html')


def category(request):
    return render(request, 'article/category.html')


def publish(request):
    return render(request, 'article/publish.html')

