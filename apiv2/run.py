import os

from source.app import create_app

if __name__ == '__main__':  # If the file and main names are the same
    '''Call the function and pass our environment name'''
    define_env = os.getenv('FLASK_ENV')
    app = create_app(define_env)

    app.run()
