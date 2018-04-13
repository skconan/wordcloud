from django.urls import path, include
from . import views

app_name = 'process'

urlpatterns = [
    path('process/', views.process),
]