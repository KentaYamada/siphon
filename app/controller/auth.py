from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.user import User
from app.model.mapper.user_mapper import UserMapper

bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/', methods=['POST'])
def login():
    res = ResponseBody()
    if request.json is None:
        res.set_fail_response(400)
        return res
    if not request.json.keys() >= {'email', 'password'}:
        res.set_fail_response(400)
        return res

    hashed_password = request.json.get('password')
    user = User(
        email=request.json.get('email'),
        password=hashed_password
    )
    mapper = UserMapper()
    auth_user = None
    try:
        auth_user = mapper.find_auth_user(user)
    except Exception as e:
        # todo: logging
        print(e)
        res.set_fail_response(500)
    if auth_user is None:
        res.set_fail_response(403)
    else:
        res.set_success_response(200)
    return res


@bp.route('/logout', methods=['POST'])
def logout():
    pass
