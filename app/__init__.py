from flask import Flask
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import (
    BadRequest,
    Conflict,
    Forbidden,
    NotFound,
    InternalServerError,
    Unauthorized
)
from app.config import get_config
from app.libs.error_handler import api_error_handler
from app.controller import auth
from app.controller import cashier
from app.controller import category
from app.controller import daily_sales
from app.controller import dashboard
from app.controller import item
from app.controller import sales
from app.controller import user
from app.controller import view


jwt = None


def startup_app():
    app = Flask(__name__)

    # URL末尾のスラッシュを含めなくて良いようにする
    app.url_map.strict_slashes = False

    # register blueprints
    blueprints = [
        auth.bp,
        cashier.bp,
        category.bp,
        daily_sales.bp,
        dashboard.bp,
        item.bp,
        sales.bp,
        user.bp,
        view.bp
    ]

    for bp in blueprints:
        app.register_blueprint(bp)

    # register error handlers
    app.register_error_handler(BadRequest, api_error_handler)
    app.register_error_handler(Conflict, api_error_handler)
    app.register_error_handler(Forbidden, api_error_handler)
    app.register_error_handler(InternalServerError, api_error_handler)
    app.register_error_handler(NotFound, api_error_handler)
    app.register_error_handler(Unauthorized, api_error_handler)

    # todo: configの読み込み箇所ここ？
    app.config.from_object('app.config.DevelopmentConfig')

    # 一旦仮で
    global jwt
    jwt = JWTManager(app)

    return app
