from django.db import models

# Create your models here.

class Program(models.Model):
    PROGRAM_TYPES = [
        ('primary', 'Primary School'),
        ('secondary', 'Secondary School'),
        ('high', 'High School'),
    ]
    
    name = models.CharField(max_length=200)
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPES)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    curriculum = models.TextField(help_text="Curriculum overview")
    requirements = models.TextField(help_text="Admission requirements", blank=True)
    image = models.ImageField(upload_to='programs/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['program_type', 'name']
    
    def __str__(self):
        return self.name

class AcademicCalendar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    event_type = models.CharField(max_length=50, choices=[
        ('holiday', 'Holiday'),
        ('exam', 'Examination'),
        ('event', 'School Event'),
        ('break', 'School Break'),
    ])
    
    class Meta:
        ordering = ['start_date']
    
    def __str__(self):
        return self.title

class Subject(models.Model):
    LEVEL_CHOICES = [
        ('ordinary', 'Ordinary Level'),
        ('advanced', 'Advanced Level'),
        ('ordinaryadvanced', 'Ordinary and Advanced Levels')
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='ordinary')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['level', 'name']
    
    def __str__(self):
        return self.name