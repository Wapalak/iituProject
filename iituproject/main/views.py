from django.shortcuts import render
from django.http import Http404
from django.template import loader

def index(request):
    data = {
        'title': 'Главная страница'
    }
    try:
        # Проверяем наличие шаблона перед его рендерингом
        loader.get_template('main/index.html')
        return render(request, 'main/index.html', data)
    except loader.TemplateDoesNotExist:
        raise Http404

def about(request):
    try:
        loader.get_template('main/about.html')
        return render(request, 'main/about.html')
    except loader.TemplateDoesNotExist:
        raise Http404
