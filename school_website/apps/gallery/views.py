from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import GalleryImage, GalleryCategory

class GalleryView(ListView):
    model = GalleryImage
    template_name = 'gallery/index.html'
    context_object_name = 'images'
    paginate_by = 12
    
    def get_queryset(self):
        category_id = self.request.GET.get('category')
        if category_id:
            return GalleryImage.objects.filter(category_id=category_id)
        return GalleryImage.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GalleryCategory.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context