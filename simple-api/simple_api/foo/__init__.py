# coding: utf-8

from flask import Blueprint

bp = foo_bp = Blueprint('foo', __name__, url_prefix='/foo')

from . import endpoints, tasks
