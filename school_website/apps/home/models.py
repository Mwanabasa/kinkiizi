from django.db import models

# Create your models here.

class HomePageContent(models.Model):
    welcome_title = models.CharField(max_length=200)
    welcome_message = models.TextField()
    principal_message = models.TextField()
    head_teacher_photo = models.ImageField(upload_to='home/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Home Page Content"
    
    def __str__(self):
        return "Home Page Content"