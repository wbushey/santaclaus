# -*- coding: utf8 -*-
from __future__ import absolute_import, unicode_literals
from faker import Faker
import json
import os
import tempfile
import unittest
from santaclaus import app, db
from santaclaus.models import Person


class SantaClausTest(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['SQLALCHEMY_DATABASE_URL'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()
        self.fake = Faker()

    def tearDown(self):
        pass
        os.close(self.db_fd)
        os.unlink(app.config['SQLALCHEMY_DATABASE_URL'])

    def assert_json_response(self, r):
        self.assertEqual(r.headers['Content-Type'], 'application/json')

    def test_request_with_a_name(self):
        r = self.app.get('/?name=%s' % self.fake.name().replace(" ", "%20"))

        self.assertEqual(r.status_code, 200)
        self.assert_json_response(r)
        data_js = json.loads(r.data)
        self.assertTrue('name' in data_js)
        self.assertTrue('status' in data_js)

    def test_request_without_a_name(self):
        r = self.app.get('/')

        self.assertEqual(r.status_code, 400)
        self.assert_json_response(r)
        data_js = json.loads(r.data)
        self.assertTrue('error' in data_js)

    def test_person_model_decides_status(self):
        p = Person(self.fake.name())
        self.assertTrue(p.status in ['Naughty', 'Nice'])

    def test_status_ratio(self):
        naughties = 0
        for i in range(100):
            p = Person(self.fake.name())
            if p.status == 'Naughty':
                naughties = naughties + 1

        # Computer randomness is far from perfect, so let's test in a range
        self.assertTrue(naughties > 40 and naughties < 60)
