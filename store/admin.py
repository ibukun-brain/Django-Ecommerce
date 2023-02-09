from django.contrib import admin
from store.models import (
    Category, Order, OrderItem, 
    Payment, Product, SizeVariation,
    ColorVariation
)
@admin.register(SizeVariation)
class SizeVariationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['created_at']

@admin.register(ColorVariation)
class ColorVariationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['created_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    list_filter = ['created_at','updated_at']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_currency', 'stock', 'updated_at']
    list_filter  = ['created_at', 'is_available']
    date_hierarchy = 'created_at'
    search_fields = ['name']
    # filter_horizontal = ['categories', 'available_sizes', 'available_colors']
    filter_horizontal = ['categories', 'available_sizes']

    

    def price_currency(self, object):
        return f"₦{object.price}"

    price_currency.short_description = 'price'        

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display_links = ['user', 'created_at']
    list_display = [
        'user', 'created_at', 
        'ordered_date', 'ordered', 
        'address']
    autocomplete_fields = ['user','address']
    search_fields = [
        'user', 'address__address_line_1',
        'address__address_line_2']
    list_filter = ['ordered', 'ordered_date', 'created_at']
    date_hierarchy = 'created_at'
    list_select_related = ['user','address']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    # list_display = ['product', 'order', 'quantity', 'color', 'size']
    list_display = ['product', 'order', 'quantity', 'size']
    list_select_related = ['product', 'order', 'size']
    # list_select_related = ['product', 'order', 'color', 'size']
    autocomplete_fields = ['product', 'order']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['product__name', 'order__name']
    # autocomplete_fields = ['product', 'order', 'color', 'size']
    autocomplete_fields = ['product', 'order', 'size']
    date_hierarchy = 'created_at'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_method', 'amount']
    list_select_related = ['order']
    search_fields = ['order']
    autocomplete_fields = ['order']
    date_hierarchy = 'created_at'
    list_filter = ['payment_method', 'successful']