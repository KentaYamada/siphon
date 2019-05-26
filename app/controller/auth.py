from flask import request, Blueprint
from werkzeug.exceptions import BadRequest, Conflict, Forbidden, NotFound
from werkzeug.security import check_password_hash
from app.libs.api_response import ApiResponse
from app.controller.response import ResponseBody
from app.model.user import User
from app.model.mapper.user_mapper import UserMapper


bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/', methods=['POST'])
def login():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()
    if not request_data.keys() >= {'email', 'password'}:
        raise BadRequest()

    mapper = UserMapper()
    user = User(email=request.json.get('email'))

    auth_user = mapper.find_auth_user(user)
    if auth_user is None:
        raise Forbidden()

    verify_pw = check_password_hash(
        auth_user['password'],
        request.json.get('password')
    )
    if not verify_pw:
        raise Forbidden()

    auth_token = User.generate_auth_token(auth_user['id'])

    return ApiResponse(201, data={'auth_token': auth_token.decode()})


@bp.route('/logout', methods=['POST'])
def logout():
    pass


def verify_password(user, password):
    return check_password_hash(user['password'], password)
