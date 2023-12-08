from django.shortcuts import render
from .models import Articles


def reviews(request):
    reviews = Articles.objects.all()
    return render(request, 'reviews/reviews_home.html', {'reviews': reviews})
    # Вывод наших отзывов с быза данных articles


def create(request):
    return render(request, 'reviews/create.html')
