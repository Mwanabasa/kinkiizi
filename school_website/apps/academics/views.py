from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Program, AcademicCalendar, Subject

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


class ProgramDetailView(TemplateView):
    template_name = 'academics/program_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        program_type = self.kwargs.get('program_type')
        program = get_object_or_404(Program, program_type=program_type, is_active=True)
        context['program'] = program
        return context

class CalendarView(ListView):
    model = AcademicCalendar
    template_name = 'academics/calendar.html'
    context_object_name = 'events'

class SubjectListView(ListView):
    model = Subject
    template_name = 'academics/subjects.html'
    context_object_name = 'subjects'
    
    def get_queryset(self):
        return Subject.objects.filter(is_active=True)