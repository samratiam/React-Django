from django.contrib import admin

from .product.models import Product

from .category.models import Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)