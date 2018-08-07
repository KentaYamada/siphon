from flask import Flask
from app.controller import view

def startup_app():
    app = Flask(__name__)

    # todo: register blueprints
    app.register_blueprint(view.bp)


    return app
