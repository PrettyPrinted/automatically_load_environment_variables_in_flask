# demo/__init__.py
from flask import Flask 

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return f'API_KEY = { app.config.get("API_KEY") }'

    return app