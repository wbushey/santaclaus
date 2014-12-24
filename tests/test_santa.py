# -*- coding: utf8 -*-
from __future__ import absolute_import, unicode_literals
import json
import os
import tempfile
import unittest
from santaclaus import app, db

class SantaClausTest(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['SQLALCHEMY_DATABASE_URL'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        pass
        os.close(self.db_fd)
        os.unlink(app.config['SQLALCHEMY_DATABASE_URL'])

    def assert_json_response(self, r):
        self.assertEqual(r.headers['Content-Type'], 'application/json')

    def test_with_a_name(self):
        r = self.app.get('/?name=Somebody')

        self.assertEqual(r.status_code, 200)
        self.assert_json_response(r)
        data_js = json.loads(r.data)
        self.assertTrue('name' in data_js)
        self.assertTrue('status' in data_js)

    def test_without_a_name(self):
        r = self.app.get('/')

        self.assertEqual(r.status_code, 400)
        self.assert_json_response(r)
        data_js = json.loads(r.data)
        self.assertTrue('error' in data_js)
