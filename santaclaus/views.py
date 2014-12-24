# -*- coding: utf8 -*-
from flask import jsonify, request
from santaclaus import app, db
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


@app.route('/', methods=['GET'])
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


@app.route('/lists/<listname>', methods=['GET'])
def get_list(listname):
    listname = listname.capitalize()
    app.logger.info("Requst for list '%s'" % listname)
    if listname not in Person.statuses:
        rtn = {'error': "I don't keep a '%s' list" % listname}
        return jsonify(rtn), 400

    l = [p.name for p in Person.query.filter_by(status=listname)]
    rtn = {
        'list_name': listname,
        'list': l
        }
    return jsonify(rtn), 200
