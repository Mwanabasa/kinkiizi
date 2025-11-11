from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    school_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    map_embed_code = models.TextField(help_text="Embed code for Google Maps")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return "Contact Information"

class SiteSettings(models.Model):
    """Site-wide settings for footer and other global content"""
    school_description = models.TextField(
        help_text="Description displayed in the footer"
    )
    facebook_url = models.URLField(blank=True, null=True, help_text="Facebook page URL")
    twitter_url = models.URLField(blank=True, null=True, help_text="Twitter profile URL")
    instagram_url = models.URLField(blank=True, null=True, help_text="Instagram profile URL")
    linkedin_url = models.URLField(blank=True, null=True, help_text="LinkedIn page URL")
    school_hours_weekdays = models.CharField(
        max_length=100, 
        default="Monday - Friday: 8:00 AM - 3:00 PM",
        help_text="Weekday hours (e.g., Monday - Friday: 8:00 AM - 3:00 PM)"
    )
    school_hours_saturday = models.CharField(
        max_length=100, 
        default="Saturday: 9:00 AM - 12:00 PM",
        help_text="Saturday hours"
    )
    school_hours_sunday = models.CharField(
        max_length=100, 
        default="Sunday: Closed",
        help_text="Sunday hours"
    )
    copyright_text = models.CharField(
        max_length=200, 
        default="© 2024 Our School. All rights reserved.",
        help_text="Copyright text displayed in footer"
    )
    privacy_policy_url = models.URLField(blank=True, null=True, help_text="Privacy Policy page URL")
    terms_of_service_url = models.URLField(blank=True, null=True, help_text="Terms of Service page URL")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.subject} - {self.name}"