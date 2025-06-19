from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header="Ecommerce Admin Panel"


admin_site=CustomAdminSite()