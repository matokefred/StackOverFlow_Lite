from flask import Flask, make_response, jsonify
import psycopg2 as psycopg
import os
from .config import Development, Testing

APP = Flask(__name__)

if os.environ['CONTEXT'] == 'TEST':
    APP.config.from_object(Testing)
elif os.environ['CONTEXT'] == 'DEV':
    APP.config.from_object(Development)

CONNECT = psycopg.connect(
    database=APP.config['DB_NAME'],
    user=APP.config['DB_USER'],
    host=APP.config['DB_HOST'],
    password=APP.config['DB_PASSWORD'])

"""def CONNECT():
    return psycopg.connect(user="postgress", password="",database="apidatabase", host="localhost")"""


from source.end import endpoints

APP.register_blueprint(endpoints.PRINTS)


@APP.errorhandler(404)
def not_found(error):
    '''
    Error code 404
    '''
    return make_response(jsonify({'Error-definition': 'Not found'}), 404)


@APP.errorhandler(400)
def bad_request(error):
    ''' Error code 400
    '''
    return make_response(jsonify({'Error-definition': 'Bad Request'}), 400)


@APP.errorhandler(403)
def method_not_allowed(error):
    '''Error code 403
    '''
    return make_response(jsonify({"Error-definition": "Forbidden action"}), 403)

