from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from collection.models import Data


def collect(request):
    d = Data(id_data='4-14-2018_test', data='test test test')
    d.save()
    return HttpResponse('<h1>Page "Collection" was found</h1>')
