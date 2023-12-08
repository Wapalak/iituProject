from django.db import models

class Articles(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    review = models.CharField('Отзыв', max_length=200)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Отзыв:{self.title}'

    class Meta:
        verbose_name = 'New table'
        verbose_name_plural = 'New tables'