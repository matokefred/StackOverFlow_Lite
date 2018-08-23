'''Import os so that the secret protection key can be gotten from the environment'''
import os
from datetime import timedelta


class Development(object):
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or 'simplicityisthegame'
    DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_VERIFY_EXPIRATION = True
    JWT_EXPIRATION_DELTA = timedelta(seconds=1200)
    DB_NAME = 'apidb'
    DB_HOST = 'localhost'
    DB_PASSWORD = ''
    DB_USER = 'postgres'
    TRACK_MODIFICATIONS = True
    JWT_AUTH_URL_RULE = '/apiv12/auth/login'
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_ENDPOINT = 'login'


class Testing(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'simplicityisthegame'
    JWT_VERIFY_EXPIRATION = True
    DB_NAME = 'apidb'
    DB_HOST = 'localhost'
    DB_PASSWORD = ''
    DB_USER = 'postgres'
    TRACK_MODIFICATIONS = True
    DEBUG = True
    JWT_EXPIRATION_DELTA = timedelta(seconds=1200)
    JWT_AUTH_URL_RULE = '/apiv2/auth/login'
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_AUTH_ENDPOINT = 'login'


'''APP_CONFIG = {
    'development': Development,
    'testing': Testing
}'''