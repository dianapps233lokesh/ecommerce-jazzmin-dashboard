from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group

class CustomAdminSite(AdminSite):
    site_header="Ecommerce Admin Panel"


admin_site=CustomAdminSite()
admin_site.register(Group)