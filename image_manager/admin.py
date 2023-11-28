from django.contrib import admin

from image_manager.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'content_type', 'created_at', 'updated_at')

    def delete_queryset(self, request, queryset):
        for image in queryset.all():
            image.delete()
