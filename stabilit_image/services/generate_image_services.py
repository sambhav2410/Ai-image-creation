from rest_framework import exceptions

from common.boilerplate import BaseService
from common.helpers import StatusCodes
from stabilit_image.repository.image_repo import ImageRepository
from stabilit_image.tasks.image_task import generate_image_task


class GenerateImageServices(BaseService):
    def __init__(self) -> None:
        self.image_repo = ImageRepository()

    def post_service(self, request, data):
        if data.get('prompts'):
            print("11111111111")
            prompts = data.get('prompts', [])
            # if len(prompts) != 3:
            #     raise exceptions.APIException("No trips found", code=StatusCodes().BAD_REQUEST)
            print("2222222222222")
            tasks = [generate_image_task.apply_async(kwargs={"prompt": str(prompt)}) for prompt in prompts]
            resp = {"task_ids": [task.id for task in tasks]}
        return self.ok(resp, StatusCodes().CREATED)
