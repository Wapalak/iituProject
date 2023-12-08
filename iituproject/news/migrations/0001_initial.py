# Generated by Django 4.2.8 on 2023-12-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('review', models.CharField(max_length=200, verbose_name='Отзыв')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]