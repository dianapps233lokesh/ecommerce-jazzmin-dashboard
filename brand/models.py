from django.db import models


class Brand(models.Model):
    brand=models.CharField(max_length=100)

