# -*- coding: utf8 -*-
from __future__ import absolute_import, unicode_literals
from santaclaus.models import Person
from santa_test_helper import SantaClausTestCase


class ModelTest(SantaClausTestCase):

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
