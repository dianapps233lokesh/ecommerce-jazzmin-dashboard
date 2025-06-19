from django.db import models
from django.contrib.auth.models import AbstractUser


class Brand(models.Model):
    name=models.CharField(max_length=100)

class CustomUser(AbstractUser):
    brand=models.ForeignKey(Brand,null=True, blank=True, on_delete=models.SET_NULL)

