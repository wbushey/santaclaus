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
        self.assertTrue(naughties > 15 and naughties < 35)

    def test_valid_list_requests(self):
        persons = {
            'Naughty': [],
            'Nice': []
        }

        for i in range(10):
            p = Person(self.fake.name())
            persons[p.status].append(p.name)
            db.session.add(p)
        db.session.commit()

        naught_r = self.app.get('/lists/naughty')
        self.assert_json_response(naught_r)
        self.assertEqual(naught_r.status_code, 200)
        nice_r = self.app.get('/lists/nice')
        self.assert_json_response(nice_r)
        self.assertEqual(nice_r.status_code, 200)

        naughty_list = json.loads(naught_r.data)['list']
        nice_list = json.loads(nice_r.data)['list']
        naughty_list_complete = all(
            name in naughty_list for name in persons['Naughty'])
        nice_list_complete = all(
            name in nice_list for name in persons['Nice'])

        self.assertTrue(naughty_list_complete)
        self.assertTrue(nice_list_complete)
