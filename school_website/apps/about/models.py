from django.db import models

# Create your models here.
from django.db import models

class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    history = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    values = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return "About Page Content"

class Staff(models.Model):
    POSITION_CHOICES = [
        ('principal', 'Principal'),
        ('teacher', 'Teacher'),
        ('administrator', 'Administrator'),
        ('support', 'Support Staff'),
    ]
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    qualification = models.CharField(max_length=200)
    experience = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"