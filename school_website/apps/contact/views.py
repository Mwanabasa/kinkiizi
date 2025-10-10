from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ContactInfo
from .forms import ContactForm

class ContactView(CreateView):
    model = ContactInfo
    form_class = ContactForm
    template_name = 'contact/index.html'
    success_url = reverse_lazy('contact')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Thank you for your message! We will get back to you soon.')
        return super().form_valid(form)