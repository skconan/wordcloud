from django.urls import path, include
from . import views

app_name = 'collection'

urlpatterns = [
    path('collect/', views.collect),
]