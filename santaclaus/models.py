# -*- coding: utf8 -*-
from app import db

class Status(db.Model):
    __table__ = 'statuses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    status = db.Column(db.String())

    def __init__(self, name, status):
        self.name = name
        self.status = status
