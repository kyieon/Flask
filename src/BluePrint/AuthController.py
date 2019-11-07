# -*- coding: UTF-8 -*-

from .User import User
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

users = [
    User('user1', 'a'),
    User('user2', 'b'),
]

auth_service = Blueprint("auth", __name__, url_prefix="/auth")


@auth_service.route('/', methods=['POST'])
def auth():

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

    return jsonify({
        'access_token': create_access_token(identity=username)
    }), 200


@auth_service.route('/test', methods=['POST'])
@jwt_required
def test():
    return 'USER ID :: %s' % get_jwt_identity()
