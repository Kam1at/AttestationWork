from django.contrib import admin
from products.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'date')
