# Generated by Django 5.0 on 2023-12-08 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'New table', 'verbose_name_plural': 'New tables'},
        ),
    ]