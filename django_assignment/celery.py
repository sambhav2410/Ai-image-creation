import os

from celery import Celery


# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_assignment.settings")
app = Celery("django_assignment")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# Worker Configuration (optional, if you want to specify worker settings)
app.conf.update(worker_heartbeat=120, task_concurrency=4, worker_prefetch_multiplier=1)

print(app)
