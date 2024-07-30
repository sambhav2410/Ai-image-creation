# Django Image Generation Project

This project is a Django application that generates images using Stability AI’s Text-to-Image generation API. The image generation tasks are managed using Celery for parallel processing to ensure efficiency and responsiveness.

## Features

- Generate images based on text prompts using Stability AI's API.
- Handle image generation tasks in parallel using Celery.
- Store generated images in Cloudinary.
- Display generated images in a fixed size on the web page.

## Prerequisites

- Python 3.8+
- Django 4.2.4
- Redis (for Celery broker)
- Cloudinary account (for storing images)
- Stability AI API key

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/django-image-generation.git
    cd django-image-generation
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    Create a `.env` file in the root directory of the project and add the following environment variables:

    ```env
    SECRET_KEY=your_django_secret_key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1

    IMAGE_GENERATE_API_URL=your_stability_ai_api_url
    API_KEY=your_stability_ai_api_key

    CLOUD_NAME=your_cloudinary_cloud_name
    CLOUD_API_KEY=your_cloudinary_api_key
    CLOUD_API_SECRET=your_cloudinary_api_secret

    CELERY_BROKER_URL=redis://localhost:6379/0
    CELERY_RESULT_BACKEND=redis://localhost:6379/0
    ```

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Start Redis server:**

    Make sure Redis server is running. You can start Redis with:

    ```bash
    redis-server
    ```

7. **Start Celery worker:**

    Open a new terminal, activate the virtual environment, and start the Celery worker:

    ```bash
    celery -A django_assignment worker --loglevel=info -P gevent (for windows)
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the web application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/stabilit_image/generate` to access the image generation form.

2. **Generate images:**

    - Enter up to 3 text prompts.
    - Click the "Generate" button to submit the form.
    - The application will process the prompts and display the generated images below the form.

## Project Structure

- `django_assignment/`: Main project directory.
- `stabilit_image/`: App directory for the image generation feature.
- `templates/stabilit_image/generate_images.html`: Template for the image generation form and display.
- `stabilit_image/models.py`: Model for storing generated images.
- `stabilit_image/views.py`: Views for handling image generation and display.
- `stabilit_image/tasks.py`: Celery tasks for generating images.
- `django_assignment/settings.py`: Project settings, including Celery and Cloudinary configurations.
- `urls.py`: URL configurations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Celery](https://docs.celeryproject.org/en/stable/)
- [Stability AI](https://stability.ai/)
- [Cloudinary](https://cloudinary.com/)
