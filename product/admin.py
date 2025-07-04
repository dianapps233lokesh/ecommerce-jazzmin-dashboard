from django.contrib import admin
from .models import Product,ProductVariant
from ecomm.admin import admin_site
from django.http import HttpResponse
import csv



def export_to_csv(modeladmin,request, queryset):
    """Export selected queryset to CSV."""
    fieldnames = [field.name for field in queryset.model._meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment;filename={queryset.model.__name__}.csv'

    writer = csv.writer(response)

    # Header
    writer.writerow(fieldnames)

    for obj in queryset:
        row = [getattr(obj, field) for field in fieldnames]
        writer.writerow(row)

    return response

export_to_csv.short_description = "Export selected to CSV"



class ProductVariantInline(admin.TabularInline):
    model=ProductVariant
    extra=2




class ProductAdmin(admin.ModelAdmin):
    list_display=['product_name','brand']
    inlines=[ProductVariantInline]
    actions=[export_to_csv]
    
    def get_queryset(self,request):
        qs=super().get_queryset(request)
        # print(qs)

        if request.user.is_superuser:
            return qs
        return qs.filter(brand=request.user.brand)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if not request.user.is_superuser:
   
            if 'brand' in form.base_fields:
                form.base_fields['brand'].disabled = True
                form.base_fields['brand'].initial = request.user.brand
            if 'category' in form.base_fields:
                form.base_fields['category'].disabled = True
                form.base_fields['category'].initial = request.user.brand
        return form
    
    
    def save_model(self,request,obj,form,change):
        # print(request.user)
        # print(obj.brand)

        if not request.user.is_superuser:
            obj.brand=request.user.brand
        
        super().save_model(request,obj,form,change)

admin_site.register(Product,ProductAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    list_display=['product','desc','color','size','quantity','price']
    list_filter = ('product__category',)
    actions=[export_to_csv]

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