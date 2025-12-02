from django.contrib import admin
from .models import Program, AcademicCalendar, Subject

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'program_type', 'is_active']
    list_filter = ['program_type', 'is_active']
    search_fields = ['name', 'description']
    # Only show these fields in the admin form
    fields = ['name', 'program_type', 'description', 'is_active']

@admin.register(AcademicCalendar)
class AcademicCalendarAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'event_type']
    list_filter = ['event_type', 'start_date']
    search_fields = ['title', 'description']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'is_active']
    list_filter = ['level', 'is_active']
    search_fields = ['name', 'description']