from django.db import models


# Create your models here.
class CurrencyRate(models.Model):
    currency = models.CharField(max_length=50)  # тип валюты
    rate = models.FloatField()  # значение курса валюты
    date = models.DateField()  # дата

    def __str__(self):
        return f"{self.currency} - {self.date}"
