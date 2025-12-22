from django.db import models

# Create your models here.

class User_Model(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name

class Product_Model(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    def __str__(self):
        return self.name

class Order_Model(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    def __int__(self):
        return self.quantity
