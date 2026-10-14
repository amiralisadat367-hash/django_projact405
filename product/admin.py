from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','is_active','price']
    list_filter = ['name','is_active','price']


