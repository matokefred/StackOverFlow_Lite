'''Import os so that the secret protection key can be gotten from the environment'''
import os


class Development(object):
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URL')


class Production(object):
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URL')


APP_CONFIG = {
    'development': Development,
    'production': Production
}