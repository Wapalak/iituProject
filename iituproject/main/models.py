from django.db import models

# Create your models here.
class CurrencyRate(models.Model):
    currency = models.CharField(max_length=50)
    rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.currency} - {self.date}"