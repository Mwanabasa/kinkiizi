from django.urls import path
from .views import AboutView, StaffListView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('staff/', StaffListView.as_view(), name='staff'),
]