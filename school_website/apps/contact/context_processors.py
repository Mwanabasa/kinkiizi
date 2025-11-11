from .models import ContactInfo, SiteSettings

def site_context(request):
    """Context processor to make site-wide settings available to all templates"""
    return {
        'contact_info': ContactInfo.objects.first(),
        'site_settings': SiteSettings.objects.first(),
    }

