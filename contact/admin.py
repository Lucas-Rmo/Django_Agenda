from django.contrib import admin
from .models import Contact,Category
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","show")
    ordering = ("id",)
    search_fields = ("id","first_name","last_name")
    list_per_page = 25
    list_editable = ("first_name","last_name","show")
    list_display_links = ("id",)

@admin.register(Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("id",)
