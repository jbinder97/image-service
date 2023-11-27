from urllib.parse import unquote

from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from image_manager.api.serializer import ImageSerializer
from image_manager.models import Image


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(uploader=self.request.user)

    @action(methods=['POST'], detail=False)
    def upload(self, request):
        image_urls = request.data.get('urls', [])

        for image_url in image_urls:
            image_url = unquote(image_url)

            if Image.objects.filter(url=image_url).exists():
                image = Image.objects.get(url=image_url)
            else:
                image = Image.objects.create(url=image_url, uploader=request.user)

            image.download()

        return Response()

    @action(methods=['GET'], detail=False)
    def download(self, request):
        url = request.query_params.get('url', None)

        if url is None:
            return Response(status=400)

        if Image.objects.filter(url=url).exists():
            image = Image.objects.get(url=url)

            with open(image.image.path, 'rb') as f:
                return HttpResponse(f.read(), content_type=image.content_type)

        return Response(status=404)
