# -*- coding: utf8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///%s?check_same_thread=False' %
                               os.path.join(basedir, 'santa.db'))
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
