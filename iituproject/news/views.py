from django.shortcuts import render, redirect
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Articles
from .serializers import ArticlesSerializer
import json
import os


def news_home(request):
    # Получаем новости, сортируем по дате
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            new_article = form.save()

            # Создание бэкапа данных отзыва в формате JSON
            backup_data = {
                'title': new_article.title,
                'review': new_article.review,
                'rating': new_article.rating,
                'full_text': new_article.full_text,
                'date': new_article.date.strftime("%Y-%m-%d %H:%M:%S")
                # Добавьте другие поля вашей модели, если нужно
            }

            # Путь к файлу для сохранения бэкапа данных
            backup_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                            'backup', 'reviews_backup.json')

            # Запись данных в файл
            with open(backup_file_path, 'a+', encoding='utf-8') as backup_file:
                backup_file.write(json.dumps(backup_data, ensure_ascii=False) + '\n')

            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'

    else:
        form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)


# Представление для получения списка новостей в виде JSON через API
@api_view(['GET'])
def api_news_list(request):
    news = Articles.objects.order_by('-date')
    serializer = ArticlesSerializer(news, many=True)
    return Response(serializer.data)


# Представление для создания новости через API
@api_view(['POST'])
def api_create_news(request):
    if request.method == 'POST':
        serializer = ArticlesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Дополнительные действия, если нужно сохранять бэкапы или выполнять другие операции
            return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
