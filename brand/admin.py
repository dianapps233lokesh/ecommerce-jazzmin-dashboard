from django.contrib import admin
from ecomm.admin import admin_site
from .models import Brand,CustomUser
from django.contrib.auth.admin import UserAdmin




class CustomUserAdmin(UserAdmin):
    # model = CustomUser

    list_display = ('username', 'email', 'brand', 'is_staff', 'is_superuser')


    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     ('Personal info', {'fields': ('email',)}),
    #     ('Brand Info', {'fields': ('brand',)}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                 'groups', 'user_permissions')}),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'brand', 'is_staff', 'is_superuser'),
        }),
    )

admin_site.register(Brand)
admin_site.register(CustomUser, CustomUserAdmin)

# admin_site.register(CustomUser)