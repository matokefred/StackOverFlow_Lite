'''
Define all the authentication requirements
'''
import re
from flask import request, jsonify, make_response, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt import JWT

from . import CONNECT, APP
jwt = JWT()


class Users(object):
    def __init__(self, id):
        self.id = id


@APP.route('/apiv2/register', methods=['POST'])
def registration():
    '''
    Creating a new user
    '''
    if request.json and request.json['username'] and request.json['email'] and request.json['password']:
        username = request.json['username']
        email = request.json['email']
        format_email = r"(^[a-zA-Z0-9_.]+ @[a-zA-Z0-9-]+ \.[a-z]+ $)"
        password = request.json['password']
        if re.match(format_email, email):
            cursor = CONNECT.cursor()
            sqlcode = 'SELECT * FROM users WHERE email=%s;'
            cursor.execute(sqlcode, ([email]))
            collect = cursor.fetchall()
            if collect:
                return make_response(jsonify({"Bad Request": "Email address already exists"})), 400
            sqlcode = 'INSERT INTO users(username, email, password) VALUES(%s, %s, %s);'
            password = generate_password_hash(password) # Hashing the password before storage
            cursor.execute(sqlcode, (username, email, password))
            CONNECT.commit()
            return jsonify({"Success": "User account added successfully"}), 201
        return jsonify({"Bad request": "The email format that was entered is invalid"})
    abort(400)


@jwt.authentication_handler
def login(username, password):
    '''
    An already registered user can login
    '''
    cursor = CONNECT.cursor()
    sqlcode = 'SELECT * FROM users WHERE username = %s;'
    cursor.execute(sqlcode, ([username]))
    detail = cursor.fetchall()
    try:
        if check_password_hash(detail[0][3], password):
            return Users(id=detail[0][1])
        return False
    except IndexError:
        return False


@jwt.handle_displayname
def display(payload):
    '''
    The define the name of the current user
    '''
    username = payload['name']
    sqlcode = 'SELECT * FROM users WHERE username=%s;'
    cursor = CONNECT.cursor()
    cursor.execute(sqlcode, ([username]))
    detail = cursor.fetchall()
    cursor.close()
    return detail[0][0]


jwt = JWT(APP, login, display)
