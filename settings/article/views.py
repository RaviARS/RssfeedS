from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    print("hi im index")
    return render(request, 'home/home.html')

