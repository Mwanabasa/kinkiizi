from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Program, AcademicCalendar

class AcademicsView(TemplateView):
    template_name = 'academics/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programs'] = Program.objects.filter(is_active=True)
        return context

class ProgramListView(ListView):
    model = Program
    template_name = 'academics/programs.html'
    context_object_name = 'programs'
    
    def get_queryset(self):
        return Program.objects.filter(is_active=True)

class CalendarView(ListView):
    model = AcademicCalendar
    template_name = 'academics/calendar.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return AcademicCalendar.objects.all()