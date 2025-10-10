from django.contrib import admin
from .models import AboutPage, Staff

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_at']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_active']
    list_filter = ['position', 'is_active']
    search_fields = ['name', 'qualification']