import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.project.settings.development')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
