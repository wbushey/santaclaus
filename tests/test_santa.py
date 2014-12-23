# -*- coding: utf8 -*-
from __future__ import absolute_import, unicode_literals
import santaclaus
import unittest
import json

class SantaClausTest(unittest.TestCase):

    def setUp(self):
        santaclaus.app.config['TESTING'] = True
        self.app = santaclaus.app.test_client()

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
