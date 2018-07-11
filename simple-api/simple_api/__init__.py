# coding: utf-8
import datetime
import platform

from celery import Celery
from flask import Flask, request
from flask_caching import Cache
from flask_cors import CORS
from flask_mongoengine import MongoEngine


cache = Cache()
cors = CORS()
db = MongoEngine()


def init_cache(app, cache):
    cache.init_app(app, config={
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': app.config['CACHE_REDIS_URL'],
    })


def init_cors(app, cors):
    cors.init_app(app)


def init_db(app, db):
    db.init_app(app)


def make_celery(app):
    celery = Celery(app.import_name)
    celery.config_from_object('simple_api.celeryconfig')
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app():
    app = Flask(__name__)
    app.config.from_object('simple_api.config')

    init_cache(app, cache)
    init_cors(app, cors)
    init_db(app, db)

    from . import tasks

    from . import foo
    from . import bar
    app.register_blueprint(foo.bp)
    app.register_blueprint(bar.bp)

    app.celery = make_celery(app)

    # core endpoints

    @app.before_request
    def activate_celery():
        app.celery.set_current()

    @app.errorhandler(404)
    def page_not_found(exc):
        return f'Page not found: {request.path}', 404

    @app.route('/')
    def index():
        hostname = platform.node()
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        return f'You hit "{hostname}" at {now}, path: {request.path}'

    @app.route('/health')
    def health():
        return 'OK'

    @app.route('/celery_task')
    def celery_task():
        tasks.sleep.delay('Hello World')
        return 'OK'

    return app
