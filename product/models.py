from django.db import models

class Product(models.Model):
    product_name=models.CharField(max_length=200)
    brand=models.ForeignKey('brand.Brand',on_delete=models.CASCADE)
    price=models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class ProductVariant(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)
    # brand=models.ForeignKey('brand.Brand',on_delete=models.CASCADE)
    desc=models.CharField(max_length=200, null=True, blank=True)
    color=models.CharField(max_length=200,null=True)
    size=models.IntegerField(blank=True,null=True)
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.product_name}    --      {self.color}    --      {self.size}"