import base64
from celery import shared_task
import requests
from cloudinary.uploader import upload

from django_assignment import settings
from stabilit_image.models import GeneratedImage
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

cloudinary.config(
    cloud_name="dk2swp4ll",
    api_key="145515339268849",
    api_secret="O09F9xaxR9HcCAMJU_4jHCq1vYM",
    secure=True
)


@shared_task
def generate_image_task(prompt):
    print("1111111111111111111")
    api_url = settings.image_generate_api_url
    api_key = settings.api_key
    print("api key", api_key, api_url)

    payload = {
        "text_prompts": [
            {"text": prompt}
        ],
        "cfg_scale": 7,
        "height": 640,
        "width": 1536,
        "samples": 1,
        "steps": 30
    }
    print("payload", payload)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    print("333333")
    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        artifacts = data.get('artifacts', [])
        if artifacts:
            base64_image = artifacts[0].get('base64')
            image_binary = base64.b64decode(base64_image)
            upload_result = upload(image_binary, folder="generated_images", public_id=prompt.replace(' ', '_'))
            image_url = upload_result['secure_url']
            image = GeneratedImage.objects.create(prompt=prompt, image_url=image_url)
            print("image", image)
            return data
    else:
        return {"error": response.text}
