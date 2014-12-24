# -*- coding: utf8 -*-
from __future__ import absolute_import, unicode_literals
import json
from santaclaus import db
from santaclaus.models import Person
from santa_test_helper import SantaClausTestCase


class SantaClausV1Test(SantaClausTestCase):

    def test_request_with_a_name(self):
        r = self.app.get('/api/v1/status/?name=%s' % self.fake.name().replace(" ", "%20"))

        self.assertEqual(r.status_code, 200)
        self.assert_json_response(r)
        data_js = json.loads(r.data)
        self.assertTrue('name' in data_js)
        self.assertTrue('status' in data_js)

    def test_request_without_a_name(self):
        r = self.app.get('/api/v1/status/')

        self.assertEqual(r.status_code, 400)
        self.assert_json_response(r)
        data_js = json.loads(r.data)
        self.assertTrue('error' in data_js)

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

        naught_r = self.app.get('/api/v1/lists/naughty')
        self.assert_json_response(naught_r)
        self.assertEqual(naught_r.status_code, 200)
        nice_r = self.app.get('/api/v1/lists/nice')
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
