from flask import Flask, make_response, jsonify
import psycopg2
from .config import Development


APP = Flask(__name__)
APP.config.from_object(Development)

CONNECT = psycopg2.connect(db=APP.config['DB_NAME'], user=APP.config['DB_USER'])

