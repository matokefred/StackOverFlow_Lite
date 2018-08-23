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
    DATABASE_NAME = 'apidb'
    DATABASE_HOST = 'localhost'
    DATABASE_PASSWORD = ''
    DATABASE_USER = 'postgres'
    TRACK_MODIFICATIONS = True


class Testing(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'simplicityisthegame'
    JWT_VERIFY_EXPIRATION = True
    DATABASE_NAME = 'apidb'
    DATABASE_HOST = 'localhost'
    DATABASE_PASSWORD = ''
    DATABASE_USER = 'postgres'
    TRACK_MODIFICATIONS = True
    DEBUG = True
    JWT_EXPIRATION_DELTA = timedelta(seconds=1200)


APP_CONFIG = {
    'development': Development,
    'testing': Testing
}