from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from home.models import Address, CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("password",)}),
        (
            _("Personal info"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "profile_pic",
                    "email",
                    "mobile_no",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": (
                "wide",), "fields": (
                "password1", "password2"), },), )
    
    def thumbnail(self, object):
        img = object.image_url
        return format_html('<img src="{0}" width="30"/>', img)
    thumbnail.short_description = 'Profile image'
    list_display = [
        "thumbnail",
        "first_name",
        "last_name",
        "email",
        "username",
        "is_superuser",
        "is_staff",
    ]
    ordering = ("first_name", "last_name","username")
    list_display_links = ["first_name", "email"]
    list_filter = ["date_joined"]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address_line_1', 'address_line_2','city', 'state', 'zip_code']
    list_select_related = ['user']
    list_filter = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'
    autocomplete_fields = ['user']
    search_fields = ['user', 'address_line_1', 'address_line_2']
