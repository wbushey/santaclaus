# -*- coding: utf8 -*-
from santaclaus import app, db
from flask import jsonify, request
from .models import Person


def get_status(name):

    person = Person.query.filter_by(name=name).first()
    if person is None:
        person = Person(name)
        db.session.add(person)
        db.session.commit()
        app.logger.info('Remembering that %s is %s' % (person.name,
                        person.status))

    return {'name': person.name,
            'status': person.status}


@app.route('/', methods=['GET', 'POST'])
def index():
    rtn = {}
    status = 400

    name = ''
    if request.method == 'GET':
        name = request.args.get('name', '')
    else:
        name = request.form['name']

    if not name:
        rtn = {'error': "Must provide 'name' parameter"}
        status = 400
    else:
        rtn = get_status(name)
        status = 200

    return jsonify(rtn), status
