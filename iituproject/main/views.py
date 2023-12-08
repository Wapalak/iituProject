from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Success<h1>")

def about(request):
    return HttpResponse("<h1>Z O V<h1>")