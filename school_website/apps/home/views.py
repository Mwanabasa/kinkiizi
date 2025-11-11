# apps/home/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from gallery.models import GalleryImage
from news.models import News
from .models import HomePageContent

class HomeView(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get only published news, ordered by most recent
        context['latest_news'] = News.objects.filter(is_published=True)[:3]
        context['gallery_images'] = GalleryImage.objects.all()[:12]
        # Get the home page content (there should only be one instance)
        context['home_content'] = HomePageContent.objects.first()
        return context

# Temporary simple view for testing
def home_view(request):
    return render(request, 'home/index.html')