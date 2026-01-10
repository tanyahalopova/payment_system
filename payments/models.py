from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='usd')

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price)

    def get_stripe_price(self):
        return int(self.price * 100)