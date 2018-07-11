# coding: utf-8

from flask import jsonify, request

from simple_api.foo import foo_bp, tasks
from simple_api.models import User


@foo_bp.route('/users', methods={'POST'})
def create_user():
    user = User(**request.json)
    user.save()
    return jsonify(user)


@foo_bp.route('/users/<username>', methods={'GET'})
def get_user(username):
    user = User.objects.get(username=username)
    return jsonify(user)


@foo_bp.route('/celery_task')
def celery_task():
    tasks.sleep.delay('Hello World')
    return 'OK'
