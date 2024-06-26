import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.project.settings.development')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()



app.conf.beat_schedule = {
    'auto-assigning-fine-every-day': {
        'task': 'core.apps.books.tasks.auto_assigning_fine',
        'schedule': crontab(hour=0, minute=0),
    },
}