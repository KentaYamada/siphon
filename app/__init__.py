from flask import Flask
from app.controller import cashier
from app.controller import monthly_sales
from app.controller import user
from app.controller import view


def startup_app():
    app = Flask(__name__)

    blueprints = [
        cashier.bp,
        monthly_sales.bp,
        user.bp,
        view.bp
    ]

    for bp in blueprints:
        app.register_blueprint(bp)

    return app
