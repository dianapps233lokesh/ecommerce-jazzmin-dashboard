from django.contrib import admin
from ecomm.admin import admin_site
from .models import Brand,CustomUser,Category
from django.contrib.auth.admin import UserAdmin



class CategoryInline(admin.TabularInline):
    model=Category
    extra=2

class CustomUserAdmin(UserAdmin):
    # model = CustomUser
    
    list_display = ('username', 'email', 'brand', 'is_staff', 'is_superuser')
    readonly_fields=['username','email','last_login','date_joined']
    # exclude=['user_permissions']

    def get_readonly_fields(self, request, obj = None):
        if obj:
            return ['username','email','last_login','date_joined']
        return ['last_login','date_joined']

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets=super().get_fieldsets(request,obj)
            modified=[]
            for name,dict_ in fieldsets:
                fields=dict_.get("fields",[])
                if 'password' in fields:
                    fields=tuple(f for f in fields if f!='password')
                modified.append((name,{"fields":fields}))

        if obj and obj == request.user and request.user.is_superuser:
            # remove 'user_permissions' from all fieldsets
            new_fieldsets = []
            for name, opts in modified:
                fields = opts.get('fields', [])
                if 'user_permissions' in fields:
                    fields = tuple(f for f in fields if f != 'user_permissions')
                new_fieldsets.append((name, {**opts, 'fields': fields}))
            return new_fieldsets

        return fieldsets

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'brand', 'is_staff', 'is_superuser'),
        }),
    )

admin_site.register(CustomUser, CustomUserAdmin)

class BrandAdmin(admin.ModelAdmin):
    inlines=[CategoryInline]

admin_site.register(Brand,BrandAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display=['brand','name']

    def get_queryset(self,request):
        qs=super().get_queryset(request)
        

        if request.user.is_superuser:
            return qs
        return qs.filter(brand=request.user.brand)

admin_site.register(Category,CategoryAdmin)