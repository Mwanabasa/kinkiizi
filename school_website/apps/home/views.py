# apps/home/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Temporarily remove the imports that cause circular dependencies
        context['latest_news'] = []  # Empty for now
        context['gallery_images'] = []  # Empty for now
        context['home_content'] = None  # Empty for now
        return context

# Temporary simple view for testing
def home_view(request):
    return render(request, 'home/index.html')