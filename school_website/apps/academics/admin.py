from django.contrib import admin
from .models import Program, AcademicCalendar

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'program_type', 'duration', 'is_active']
    list_filter = ['program_type', 'is_active']
    search_fields = ['name', 'description']

@admin.register(AcademicCalendar)
class AcademicCalendarAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'event_type']
    list_filter = ['event_type', 'start_date']
    search_fields = ['title', 'description']