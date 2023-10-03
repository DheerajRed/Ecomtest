from django.db import models

# Create your models here.
class Products(models.Model):
    product_name= models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_price = models.IntegerField()


class Cart(models.Model):
    product_name= models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_price = models.IntegerField()
   


