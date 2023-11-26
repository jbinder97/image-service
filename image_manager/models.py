from django.db import models

from image_service import settings


class Image(models.Model):
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

    def download(self):
        from urllib import request
        from django.core.files.base import ContentFile

        image_url = self.url

        response = request.urlopen(image_url)
        content_type = response.getheader('Content-Type')

        if 'image' in content_type:
            self.image.save(
                image_url.split('/')[-1],
                ContentFile(response.read())
            )
            self.content_type = content_type

            self.save()
