# coding=utf-8

from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={ 'hello_world': 'Hello World'})