from django.urls import path
from . import views
from .views import api_news_list, api_create_news

urlpatterns = [
    # Главная страница отзывов
    path('', views.news_home, name='news_home'),

    # Создание отзыва
    path('create/', views.create, name='create'),

    # Детали отзыва
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    # REST framework лист отзывов
    path('api/news/create/', api_create_news, name='api-create-news'),
    # REST framework создание отзыва
    path('api/news/', views.api_news_list, name='api-news-list'),

]
