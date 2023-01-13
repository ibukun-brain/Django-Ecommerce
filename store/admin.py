from django.contrib import admin
from store.models import (
    Category, Order, OrderItem, 
    Payment, Product
)

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
    filter_horizontal = ['categories']

    def price_currency(self, object):
        return f"₦{object.price}"

    price_currency.short_description = 'price'        

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display_links = ['user', 'created_at']
    list_display = [
        'user', 'created_at', 
        'ordered_date', 'ordered', 
        'billing_address', 'shipping_address']
    autocomplete_fields = ['user','billing_address','shipping_address']
    search_fields = [
        'user', 'billing_address__address_line_1',
        'billing_address__address_line_2','shipping_address__address_line_1',
        'shipping_address__address_line_2']
    list_filter = ['ordered', 'ordered_date', 'created_at']
    date_hierarchy = 'created_at'
    list_select_related = ['user','billing_address', 'shipping_address']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity']
    list_select_related = ['product', 'order']
    autocomplete_fields = ['product', 'order']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['product__name', 'order__name']
    autocomplete_fields = ['product', 'order']
    date_hierarchy = 'created_at'


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'payment_method', 'amount']
    list_select_related = ['order']
    search_fields = ['order']
    autocomplete_fields = ['order']
    date_hierarchy = 'created_at'
    list_filter = ['payment_method', 'successful']