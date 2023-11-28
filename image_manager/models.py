import os
import uuid

from django.db import models

from image_service import settings

SUPPORTED_CONTENT_TYPES = [
    'image/jpeg',
    'image/png',
]


class Image(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        auto_created=True,
    )

    url = models.URLField(primary_key=True)

    image = models.ImageField(upload_to='images/')

    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='uploaded_images'
    )

    content_type = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        if self.image:
            print(self.image.path)
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        super().delete(*args, **kwargs)

    def download(self):
        from urllib import request
        from django.core.files.base import ContentFile

        image_url = self.url

        response = request.urlopen(image_url)
        content_type = response.getheader('Content-Type')

        if content_type in SUPPORTED_CONTENT_TYPES:
            self.content_type = content_type

            filename = str(self.uuid) + '.' + content_type.split('/')[-1]

            self.image.save(
                filename,
                ContentFile(response.read())
            )

            self.save()
