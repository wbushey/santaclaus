from santaclaus import app
from flask import jsonify, request
import random

statuses = [
    "Naughty",
    "Nice",
]


def naughty_or_nice(name):
    status = random.choice(statuses)
    rtn = {'name': name,
           'status': status}
    return rtn


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
        rtn = naughty_or_nice(name)
        status = 200

    return jsonify(rtn), status
