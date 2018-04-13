from django.urls import path, include
from . import views

app_name = 'display'

urlpatterns = [
    path('display/', views.display),
]