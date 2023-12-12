from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)  # Поле для хранения названия статьи
    review = models.CharField('Цель кредита', max_length=200)  # Поле для хранения цели кредита
    rating = models.TextField('Рейтинг', max_length=10)  # Поле для хранения рейтинга статьи
    full_text = models.TextField('Текст')  # Поле для хранения полного текста статьи
    date = models.DateTimeField('Дата публикации', auto_now_add=True)  # Поле для хранения даты публикации статьи

    def __str__(self):
        return self.title  # Метод для возврата строкового представления объекта (в данном случае, названия статьи)

    class Meta:
        verbose_name = 'Отзыв'  # Название модели в единственном числе для админки
        verbose_name_plural = 'Отзывы'  # Название модели во множественном числе для админки
