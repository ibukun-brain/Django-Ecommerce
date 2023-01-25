from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

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
    list_display = [
        "first_name",
        "last_name",
        "email",
        "username",
        "mobile_no",
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
