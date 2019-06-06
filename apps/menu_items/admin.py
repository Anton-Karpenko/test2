from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name"]
