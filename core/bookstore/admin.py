from django.contrib import admin

from .models import Product, Order, Category

# Register your models here.
from django.contrib import admin
from core.bookstore.models import *
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ['product', 'user']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active')
    search_fields = ['product_id', 'title']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'active')
    list_filter = ('active',)
    search_fields = ['title', 'active']


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
