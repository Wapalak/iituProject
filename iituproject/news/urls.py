from django.urls import path
from . import views

urlpatterns = [
    # Главная страница отзывов
    path('', views.news_home, name='news_home'),

    # Создание отзыва
    path('create/', views.create, name='create'),

    # Детали отзыва
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
]
