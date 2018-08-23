import os

from source.app import APP

if __name__ == '__main__':  # If the file and main names are the same
    '''Call the function and pass our environment name'''
    define_env = os.getenv('FLASK_ENV')

