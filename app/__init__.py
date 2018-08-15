from flask import Flask
from app.controller import view, monthly_sales


def startup_app():
    app = Flask(__name__)

    blueprints = [
        view.bp,
        monthly_sales.bp
    ]

    for bp in blueprints:
        app.register_blueprint(bp)

    return app
