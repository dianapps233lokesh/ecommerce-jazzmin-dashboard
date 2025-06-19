from django.contrib import admin
from ecomm.admin import admin_site
from .models import Brand,CustomUser


admin_site.register(Brand)