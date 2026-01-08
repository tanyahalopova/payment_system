from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # Цена в основных единицах (например, доллары)
    currency = models.CharField(max_length=3, default='usd') # Бонус: валюта

    def __str__(self):
        return self.name
