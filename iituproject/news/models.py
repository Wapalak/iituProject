from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)  # Название статьи
    review = models.CharField('Цель кредита', max_length=200)  # Цель кредита
    rating = models.TextField('Рейтинг', max_length=10)  # Рейтинг
    full_text = models.TextField('Текст')  # Полный текст статьи
    date = models.DateTimeField('Дата публикации', auto_now_add=True)  # Дата публикации статьи


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'