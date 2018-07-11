# coding: utf-8
import datetime

from simple_api import db


class User(db.Document):
    username = db.StringField(unique=True, sparse=True, regex=r'^[a-z0-9][a-z0-9\.\-_]*$')
    email = db.EmailField(max_length=256)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'index_background': True,
        'indexes': [
            {'fields': ['username']},
            {'fields': ['email']},
        ],
    }
