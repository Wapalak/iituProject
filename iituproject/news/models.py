from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)  # Название статьи
    review = models.CharField('Отзыв', max_length=200)  # Краткий отзыв
    rating = models.TextField('rating', max_length=10)  # Краткий отзыв
    full_text = models.TextField('Текст')  # Полный текст статьи
    date = models.DateTimeField('Дата публикации', auto_now_add=True)  # Дата публикации статьи


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New table'
        verbose_name_plural = 'New tables'