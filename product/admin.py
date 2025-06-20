from django.contrib import admin
from .models import Product,ProductVariant
from ecomm.admin import admin_site


class ProductVariantInline(admin.TabularInline):
    model=ProductVariant
    extra=2




class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','brand','price']
    inlines=[ProductVariantInline]
    
    def get_queryset(self,request):
        qs=super().get_queryset(request)
        print(qs)

        if request.user.is_superuser:
            return qs
        return qs.filter(brand=request.user.brand)
    
    
    def save_model(self,request,obj,form,change):
        # print(request.user)
        # print(obj.brand)

        if not request.user.is_superuser:
            obj.brand=request.user.brand
        
        super().save_model(request,obj,form,change)

admin_site.register(Product,ProductAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display=['product','desc','color','size','quantity']
    list_filter = ('product__brand',)

    def get_queryset(self,request):
        qs=super().get_queryset(request)
        # print(qs)

        if request.user.is_superuser:
            return qs
        return qs.filter(product__brand=request.user.brand)
    
    def get_form(self,request,obj=None,**kwargs):
        form=super().get_form(request,obj,**kwargs)

        if not request.user.is_superuser:
            # print(form.base_fields)

            if 'product' in form.base_fields:
                # form.base_fields['product'].disabled=True
               
                form.base_fields['product'].initial=request.user.brand
        return form



admin_site.register(ProductVariant,ProductVariantAdmin)