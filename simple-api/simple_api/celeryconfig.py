# coding: utf-8
import os


broker_url = os.environ.get('CELERY_BROKER_URL') or 'redis://127.0.0.1:6379/0'
result_backend = os.environ.get('CELERY_RESULT_BACKEND') or 'redis://127.0.0.1:6379/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

task_eager_propagates = True
task_ignore_result = True

timezone = 'UTC'
enable_utc = True
