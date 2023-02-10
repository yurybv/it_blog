from django.shortcuts import render
from django.http import HttpResponse


def home(render):
    return HttpResponse('<h1>Blog Home</h1>')
