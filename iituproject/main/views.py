from django.http import Http404, HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime, timedelta
import requests
import matplotlib.pyplot as plt
from PIL import Image
import io
from .models import CurrencyRate  # Импорт модели CurrencyRate из ваших файлов

def index(request):
    data = {'title': 'Главная страница'}

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

def get_currency_data(request):
    app_id = '184ced509b81482c9d5b700969a414e0'
    base_url = f'https://open.er-api.com/v6/latest/KZT'

    # Запрос данных о курсах валют
    response = requests.get(base_url, params={'app_id': app_id})
    if response.status_code == 200:
        data = response.json()
        currencies = ['USD', 'EUR']
        currency_data = {currency: [] for currency in currencies}

        # Получение данных о курсах валют из полученного ответа
        for currency in currencies:
            if currency in data['rates']:
                currency_data[currency].append(data['rates'][currency])

        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=6)

        # Создание списков дат и курсов для построения графика
        dates = [start_date + timedelta(days=i) for i in range(6)]
        rates_usd = [380, 385, 390, 392, 387, 499]
        rates_eur = [450, 452, 448, 445, 447, 333]

        for currency, rates in currency_data.items():
            for rate in rates:
                if currency == 'USD':
                    rates_usd.append(rate)
                elif currency == 'EUR':
                    rates_eur.append(rate)

        min_length = min(len(dates), len(rates_usd), len(rates_eur))
        dates = dates[:min_length]
        rates_usd = rates_usd[:min_length]
        rates_eur = rates_eur[:min_length]

        # Отображение графика
        plt.figure(figsize=(10, 6))
        plt.plot(dates, rates_usd, label='USD', linewidth=3)
        plt.plot(dates, rates_eur, label='EUR', linewidth=3)
        plt.xlabel('Date')
        plt.ylabel('Rate in KZT')
        plt.title('Currency Exchange Rates')
        plt.ylim(0, 700)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        img = Image.open(buffer)
        response = HttpResponse(content_type="image/png")
        img.save(response, "PNG")
        return response

    # Если запрос вернулся с ошибкой, просто вернем пустой HTTP-ответ
    return HttpResponse(status=500)

def currency_chart(request):
    return render(request, 'currency_chart.html')
