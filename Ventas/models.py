from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, default='')
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Cart(models.Model):
    products = models.ManyToManyField(Product)
    total = models.IntegerField(default=0, editable=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '$' + str(self.total) + ' ' + str(self.date_created)