from django.contrib import admin
from review.models import Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','review_title','preview', 'reviewed', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'reviewed']
    search_fields = ['review_title','user__first_name', 'user__last_name', 'user__email', 'user__username','product__name']
    list_select_related = ['user', 'order', 'product']
    autocomplete_fields = ['user', 'order', 'product']
    date_hierarchy = 'created_at'