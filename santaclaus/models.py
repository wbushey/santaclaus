# -*- coding: utf8 -*-
from santaclaus import db
import random


class Person(db.Model):
    __tablename__ = 'persons'

    statuses = [
        "Naughty",
        "Nice",
    ]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    status = db.Column(db.String())

    def __init__(self, name, status=None):
        self.name = name
        if status is None:
            status = self.decide_status()
        self.status = status

    def decide_status(self):
        if random.random() < 0.25:
            status = Person.statuses[0]
        else:
            status = Person.statuses[1]
        return status
