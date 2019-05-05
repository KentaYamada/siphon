from flask import Flask
from app.controller import auth
from app.controller import cashier
from app.controller import category
from app.controller import daily_sales
from app.controller import dashboard
from app.controller import item
from app.controller import sales
from app.controller import user
from app.controller import view


def startup_app():
    app = Flask(__name__)

    # URL末尾のスラッシュを含めなくて良いようにする
    app.url_map.strict_slashes = False
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
    return app
