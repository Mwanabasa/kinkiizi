from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import AboutPage, Staff

class AboutView(TemplateView):
    template_name = 'about/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_content'] = AboutPage.objects.first()
        return context

class StaffListView(ListView):
    model = Staff
    template_name = 'about/staff.html'
    context_object_name = 'staff_members'
    
    def get_queryset(self):
        return Staff.objects.filter(is_active=True).order_by('position', 'name')