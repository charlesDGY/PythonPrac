"""URLs module for products app."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.product_new)
]
