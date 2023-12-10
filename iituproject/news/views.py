from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.http import Http404
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
                'full_text': new_article.full_text,
                'date': new_article.date.strftime("%Y-%m-%d %H:%M:%S")
                # Добавьте другие поля вашей модели, если нужно
            }

            # Путь к файлу для сохранения бэкапа данных
            backup_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup', 'reviews_backup.json')

            # Запись данных в файл
            with open(backup_file_path, 'a+') as backup_file:
                backup_file.write(json.dumps(backup_data) + '\n')

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