from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # URL для главной страницы
    path('about/', views.about, name='about'),  # URL для страницы "О нас"
    path('get_currency_data/', views.get_currency_data, name='get_currency_data'),  # URL для получения курса валют
    path('currency_chart/', views.currency_chart, name='currency_chart'), ]  # URL для получения графика курса валют
