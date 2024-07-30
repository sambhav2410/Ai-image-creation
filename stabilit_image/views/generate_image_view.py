from django.db.transaction import atomic
from django.shortcuts import render

from common.boilerplate import BaseAPIView, validate_request
from stabilit_image.models import GeneratedImage
from stabilit_image.serializer.image_filter import GenerateImageFilterSerializer
from stabilit_image.services.generate_image_services import GenerateImageServices


class GenerateImageView(BaseAPIView):

    def __init__(self):
        self.service = GenerateImageServices()

    @atomic
    @validate_request(GenerateImageFilterSerializer)
    def post(self, request, data, *args):
        print("data", data)
        service_data = self.service.post_service(request, data)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(response_data, status_code, "Image created successfully")

    def get(self,request):
        images = GeneratedImage.objects.all().order_by("-created_at")
        return render(request, "stabilit_image/generate_images.html", {"images": images})
