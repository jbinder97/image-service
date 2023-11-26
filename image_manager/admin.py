from django.contrib import admin

from image_manager.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'content_type', 'created_at', 'updated_at')
