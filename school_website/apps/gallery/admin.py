from django.contrib import admin
from .models import GalleryCategory, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]

admin.site.register(GalleryImage)