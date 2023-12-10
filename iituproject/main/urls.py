from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # URL для главной страницы
    path('about/', views.about, name='about')  # URL для страницы "О нас"
]
