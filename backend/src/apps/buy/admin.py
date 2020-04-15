from django.contrib import admin
from .models import Orders, Products


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('date', 'products', 'quantities', 'total_price', 'delivery_method', 
    'payment_method')
    list_filter = ('payment_method', 'products')
    search_fields = ('products',)
    ordering = ['-date', ]

admin.site.register(Orders, OrdersAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'quantity', 'rating', 'description', 
    'image_url')
    list_filter = ('category',)
    search_fields = ('name', 'category',)
    ordering = ['-name', ]

admin.site.register(Products, ProductsAdmin)