from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "karisma_test.settings.development")

app = Celery("core")

app.config_from_object("karisma_test.settings.development", namespace="CELERY")


app.autodiscover_tasks()