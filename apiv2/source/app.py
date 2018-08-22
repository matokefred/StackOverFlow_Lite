from flask import Flask
from .config import APP_CONFIG


def create_app(define_env):
    '''
    the function returns an object
    '''
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG[define_env])

    @app.route('/', methods=['GET'])
    def index():
        return 'This is the first endpoint'
    return app
