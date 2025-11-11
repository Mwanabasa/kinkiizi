from django.contrib import admin
from .models import ContactInfo, ContactMessage, SiteSettings

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'updated_at']
    fieldsets = (
        ('Contact Information', {
            'fields': ('school_name', 'address', 'phone', 'email')
        }),
        ('Map', {
            'fields': ('map_embed_code',),
        }),
    )

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['copyright_text', 'updated_at']
    fieldsets = (
        ('School Description', {
            'fields': ('school_description',),
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url'),
            'classes': ('collapse',),
        }),
        ('School Hours', {
            'fields': ('school_hours_weekdays', 'school_hours_saturday', 'school_hours_sunday'),
        }),
        ('Footer', {
            'fields': ('copyright_text', 'privacy_policy_url', 'terms_of_service_url'),
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'submitted_at', 'is_read']
    list_filter = ['is_read', 'submitted_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['submitted_at']