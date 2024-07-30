from django.db import models

from common.models.base_model import BaseModel


class GeneratedImage(BaseModel):
    prompt = models.CharField(max_length=255,null=True,blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.prompt
