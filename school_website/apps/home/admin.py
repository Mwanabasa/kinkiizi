from django.contrib import admin
from .models import HomePageContent

@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ['welcome_title', 'updated_at']