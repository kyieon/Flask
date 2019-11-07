#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import datetime
from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_restplus import Api

from namespace.AuthApi import AuthNS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'test'
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'

JWTManager(app)

api = Api(app, version='1.0', title='API',
          description='Agent API',
          )

api.add_namespace(AuthNS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
