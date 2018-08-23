from flask import Flask, make_response, jsonify
import psycopg2
from .config import Development
from source.end import endpoints

APP = Flask(__name__)
APP.config.from_object(Development)

CONNECT = psycopg2.connect(
    db=APP.config['DB_NAME'],
    user=APP.config['DB_USER'],
    host=APP.config['DB_HOST'],
    password=APP.config['DB_PASSWORD']
)


APP.register_blueprint(endpoints.PRINTS)


@APP.errorhandler(404)
def not_found(error):
    '''Error code 404
    '''
    return make_response(jsonify({'Error-definition': 'Not found'}), 404)


@APP.errorhandler(400)
def bad_request(error):
    ''' Error code 400
    '''
    return make_response(jsonify({'Error-definition': 'Bad Request'}), 400)


@APP.errorhandler(405)
def method_not_allowed(error):
    '''Error code 403
    '''
    return make_response(jsonify({"Error-definition": "Forbidden action"}), 403)

