from django.urls import path
from . import views

# /utilities/___
urlpatterns = [
    path('index/', views.index),
]