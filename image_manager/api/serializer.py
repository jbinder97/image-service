from rest_framework import serializers

from image_manager.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url', 'content_type', 'image', 'created_at', 'updated_at')
