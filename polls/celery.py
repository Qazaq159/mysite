from celery import Celery

app = Celery('polls', include=['polls.periodic'])

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.autodiscover_tasks(related_name='periodic')
