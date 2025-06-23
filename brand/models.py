from django.db import models
from django.contrib.auth.models import AbstractUser


class Brand(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=300)
    

    def __str__(self):
        return f"{self.name}"

class CustomUser(AbstractUser):
    brand=models.ForeignKey(Brand,null=True,on_delete=models.SET_NULL)


    