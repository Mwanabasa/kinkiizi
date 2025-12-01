# apps/academics/urls.py
from django.urls import path
from .views import AcademicsView, ProgramListView, SubjectListView, CalendarView

urlpatterns = [
    path('', AcademicsView.as_view(), name='academics'),
    path('programs/', ProgramListView.as_view(), name='programs'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
]