# -*- coding: UTF-8 -*-

from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restplus import Resource, Namespace


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

users = [
    User('user1', 'a'),
    User('user2', 'b'),
]

AuthNS = Namespace('auth', path='/auth')


@AuthNS.route('')
@AuthNS.doc()
class Auth(Resource):

    @AuthNS.response(200, 'Success')
    @AuthNS.response(400, 'Payload Fail')
    @AuthNS.response(401, 'Auth Fail')
    @AuthNS.response(500, 'Server Error')
    def post(self):

        def __authenticate(username, password):
            print('authenticate %s %s' % (username, password))
            for user in users:
                if user.username == username and user.password == password:
                    return user

        if not request.is_json:
            return jsonify({'msg': 'Not JSON in request'}), 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)

        user = __authenticate(username, password)
        if not user:
            return jsonify({'msg': 'Bad username and password'}), 401

        return {
            'access_token': create_access_token(identity=username)
        }, 200


@AuthNS.route('/test')
class Test(Resource):

    @jwt_required
    def post(self):
        return 'USER ID :: %s' % get_jwt_identity()
