# coding=utf-8
from django.contrib import admin
from catalog.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name', 'category']
    list_filter = ['name', 'category']

admin.site.register(Product, ProductAdmin)