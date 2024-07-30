from common.boilerplate import BaseRepository
from stabilit_image.models import GeneratedImage


class ImageRepository(BaseRepository):

    def __init__(self):
        self.model = GeneratedImage
