# -*- coding: utf8 -*-
from __future__ import absolute_import, unicode_literals
from faker import Faker
import os
import tempfile
import unittest
from santaclaus import app, db


class SantaTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.config['SQLALCHEMY_DATABASE_URL'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()
        self.fake = Faker()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['SQLALCHEMY_DATABASE_URL'])

    def assert_json_response(self, r):
        self.assertEqual(r.headers['Content-Type'], 'application/json')
