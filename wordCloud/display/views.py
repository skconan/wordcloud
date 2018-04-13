from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def display(request):
    return HttpResponse('<h1>Page "Display" was found</h1>')