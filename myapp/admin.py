from django.contrib import admin

from myapp.models import Product, ProductImage

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)