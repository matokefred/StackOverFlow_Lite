#! The app module that should define the running environment
'''Implements the concept of modules by importing
environmental configurations from different files'''
import os

from apps.routes import create_app


CONFIG_NAME = os.environ.get('FLASK_ENV')
APP = create_app(CONFIG_NAME)


if __name__ == '__main__':
    APP.run()
