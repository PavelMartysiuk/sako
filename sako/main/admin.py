from django.contrib import admin

# Register your models here.
from main.models import ProductLogo, Product, Category,Contacts, Partner, About, Manufacturer

admin.site.register(ProductLogo)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Contacts)

admin.site.register(Partner)
admin.site.register(About)

admin.site.register(Manufacturer)
