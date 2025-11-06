# apps/home/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from gallery.models import GalleryImage

class HomeView(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: wire actual latest news and home content
        context['latest_news'] = []
        context['gallery_images'] = GalleryImage.objects.all()[:12]
        context['home_content'] = []
        return context

# Temporary simple view for testing
def home_view(request):
    return render(request, 'home/index.html')