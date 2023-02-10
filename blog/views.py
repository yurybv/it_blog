from django.shortcuts import render
from django.http import HttpResponse


def home(render):
    return HttpResponse('<h1>Blog Home</h1>')


def about(reqeuest):
    return HttpResponse('<h1>Blog About</h1>')
