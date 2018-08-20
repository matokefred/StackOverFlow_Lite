import os

from app.routes import create_app


config_name = os.environ.get('FLASK_ENV')
app = create_app(config_name)


if __name__ == '__main__':
    app.run()