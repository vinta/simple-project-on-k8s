# coding: utf-8
import os


SECRET_KEY = 'secret-key'

# flask-caching
CACHE_REDIS_URL = os.environ.get('CACHE_REDIS_URL') or 'redis://127.0.0.1:6379/2'

# flask-mongoengine
MONGODB_HOST = os.environ.get('MONGODB_URL') or 'mongodb://127.0.0.1/demo'
