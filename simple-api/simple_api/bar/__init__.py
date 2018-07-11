# coding: utf-8

from flask import Blueprint

bp = bar_bp = Blueprint('bar', __name__, url_prefix='/bar')

from . import endpoints, tasks
