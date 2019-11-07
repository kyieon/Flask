#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import datetime
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


users = [
    User('user1', 'a'),
    User('user2', 'b'),
]


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'test'
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'


def authenticate(username, password):
    print('authenticate %s %s' % (username, password))
    for user in users:
        if user.username == username and user.password == password:
            return user


jwt = JWTManager(app)


@app.route('/', methods=['GET'])
def testA():
    return "None Auth"


@app.route('/auth', methods=['POST'])
def auth():

    if not request.is_json:
        return jsonify({'msg': 'Not JSON in request'}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = authenticate(username, password)
    if not user:
        return jsonify({'msg': 'Bad username and password'}), 401

    return jsonify({
        'access_token': create_access_token(identity=username)
    }), 200


@app.route('/test', methods=['POST'])
@jwt_required
def test():
    return 'USER ID :: %s' % get_jwt_identity()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
