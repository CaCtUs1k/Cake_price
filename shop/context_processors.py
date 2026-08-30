from .models import SiteSettings

def site_settings(request):
    return {
        'social_settings': SiteSettings.load()
    }