from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('create', views.create, name='create'),
]
