from django.db import models

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    brand=models.CharField(max_length=100)



class ProductVariant(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    desc=models.CharField(max_length=200)
    color=