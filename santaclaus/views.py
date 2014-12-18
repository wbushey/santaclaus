from santaclaus import app
from flask import jsonify, request
import random

statuses = [
    "Naughty",
    "Nice",
]


def naughty_or_nice(name):
    if not name:
        return "Name Required"
    return random.choice(statuses)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = ''
    if request.method == 'GET':
        name = request.args.get('name', '')
    else:
        name = request.form['name']

    status = naughty_or_nice(name)
    return jsonify(name=name, 
                   status=status)
