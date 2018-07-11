# coding: utf-8

from flask import jsonify

from . import bar_bp, tasks


@bar_bp.route('/', methods={'GET'})
def index():
    return jsonify({})


@bar_bp.route('/celery_task')
def celery_task():
    tasks.sleep.delay('Hello World')
    return 'OK'
