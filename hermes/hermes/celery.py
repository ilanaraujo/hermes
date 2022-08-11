from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hermes.settings')
app = Celery('hermes')
app.conf.enable_utc=False
app.conf.update(timezone='America/Sao_Paulo')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
'envia_email': {
'task': 'hermes.tasks.envia_email',
'schedule': 120,
}
}

app.loader.override_backends['django-db'] = 'django_celery_results.backends.database:DatabaseBackend'

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')