import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'Celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SocialMedia.settings')
# Sets up the new celery application for our Django project 'awd_main'
app = Celery('SocialMedia')

# namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
