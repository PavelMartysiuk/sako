from django.contrib import admin

# Register your models here.
from main.models import ProductLogo, Product, Category, Contacts, Partner, About, Manufacturer

from django.contrib.admin.options import (
    HORIZONTAL, VERTICAL, ModelAdmin, StackedInline, TabularInline,
)

# def ProductAdmin(ModelAdmin):
#     def formfield_for_dbfield(self, db_field, request, **kwargs):
#         if db_field.name == 'description':
#             kwargs['strip'] = False
#         return super().formfield_for_dbfield(db_field, request, **kwargs)
#

admin.site.register(ProductLogo)
admin.site.register(Product, )
admin.site.register(Category)
admin.site.register(Contacts)

admin.site.register(Partner)
admin.site.register(About)

admin.site.register(Manufacturer)
