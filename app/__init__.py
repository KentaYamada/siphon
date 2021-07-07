import logging.config
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
from app.libs.jwt_handler import (
    user_loader_handler,
    user_loader_error_handler,
    token_in_blacklist_handler
)
from app.controller import auth
from app.controller import cashier
from app.controller import category
from app.controller import daily_sales
from app.controller import dashboard
from app.controller import item
from app.controller import sales
from app.controller import tax_rate
from app.controller import user
from app.controller import view


def startup_app():
    app = Flask(__name__)

    # Setup basic config.
    config = get_config()
    app.config.from_object(config)

    # Setup flask optional configs
    # URL末尾のスラッシュを含めなくて良いようにする
    app.url_map.strict_slashes = False

    # Register error handlers
    app.register_error_handler(BadRequest, api_error_handler)
    app.register_error_handler(Unauthorized, api_error_handler)
    app.register_error_handler(Forbidden, api_error_handler)
    app.register_error_handler(NotFound, api_error_handler)
    app.register_error_handler(Conflict, api_error_handler)
    app.register_error_handler(InternalServerError, api_error_handler)

    # Register blueprints
    blueprints = [
        auth.bp,
        cashier.bp,
        category.bp,
        daily_sales.bp,
        dashboard.bp,
        item.bp,
        sales.bp,
        tax_rate.bp,
        user.bp,
        view.bp
    ]

    for bp in blueprints:
        app.register_blueprint(bp)

    # Setup JWT
    jwt = JWTManager(app)

    # Register JWT handlers
    jwt.user_loader_callback_loader(user_loader_handler)
    jwt.user_loader_error_loader(user_loader_error_handler)
    jwt.token_in_blacklist_loader(token_in_blacklist_handler)

    # initialize logging
    log_option = config._get_logging_options()
    logging.config.dictConfig(log_option)

    return app
