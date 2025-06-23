from django.db import models

class Product(models.Model):
    brand=models.ForeignKey('brand.Brand',on_delete=models.CASCADE)
    category=models.ForeignKey('brand.Category',null=True,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    

    def __str__(self):
        return self.product_name


class ProductVariant(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)
    desc=models.CharField(max_length=200, null=True, blank=True)
    color=models.CharField(max_length=200, null=True, blank=True)
    size=models.CharField(max_length=50,null=True)
    quantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.product_name}    --      {self.color}    --      {self.size}"