#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_jwt import JWT, jwt_required

app = Flask(__name__)

def authenticate(username, password):
    pass

def identity(payload):
    pass

jwt = JWT(app, authenticate, identity)


@app.route('/', methods=['GET'])
def jwt_test():
    return "None Auth"

@app.route('/auth', methods=['GET'])
@jwt_required()
def jwt_test():
    return "Use Auth"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
