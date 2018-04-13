from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def collect(request):
    return HttpResponse('<h1>Page "Collection" was found</h1>')