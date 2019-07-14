from datetime import datetime
from flask import request, Blueprint
from werkzeug.exceptions import (
    BadRequest,
    InternalServerError,
    Unauthorized
)
from app.libs.api_response import ApiResponse
from app.libs.helpers import has_request_keys
from app.model.token import Token
from app.model.user import User
from app.model.mapper.auth_mapper import AuthMapper
from app.model.mapper.user_mapper import UserMapper


bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/login', methods=['POST'])
def login():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()

    request_keys = {'email', 'password'}
    if not has_request_keys(request_data, request_keys):
        raise BadRequest()

    mapper = UserMapper()
    user = User(email=request_data['email'])
    auth_user = mapper.find_auth_user(user)
    if auth_user is None:
        raise Unauthorized()

    verify_pw = User.verify_password(
        request_data['password'],
        auth_user['password']
    )
    if not verify_pw:
        # todo: error response
        raise Unauthorized(description='Invalid password')

    # ログイン済の場合は、トークンを返す
    token = __get_token(auth_user['id'])
    if token:
        data = {'logged_in': True, 'auth_token': token}
        return ApiResponse(200, data=data)

    auth_token = Token.generate_auth_token(auth_user['id'])
    token = Token(auth_user['id'], auth_token)
    saved = __save_token(token)
    if not saved:
        raise InternalServerError(description='Failed save token')

    data = {'logged_in': True, 'auth_token': auth_token}
    return ApiResponse(200, data=data)


@bp.route('/logout', methods=['POST'])
def logout():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest(description='Request data cannot be empty')

    if not has_request_keys(request_data, {'token'}):
        raise BadRequest(description='Invalid request data')

    mapper = AuthMapper()
    disposed = mapper.dispose_token(request_data['token'])
    if not disposed:
        raise InternalServerError(description='Failed dispose access token')

    data = {'logged_out': True, 'auth_token': ''}
    return ApiResponse(200, message='Logout successfully', data=data)


@bp.route('/reflesh', methods=['POST'])
def reflesh():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()

    if not has_request_keys(request_data, {'token'}):
        raise BadRequest()

    mapper = AuthMapper()
    user = mapper.find_logged_in_user(request_data['token'])
    if user is None:
        raise BadRequest(description='Requested with invalid access token')

    disposed = mapper.dispose_token(request_data['token'])
    if not disposed:
        raise InternalServerError(description='Failed dispose access token')

    auth_token = Token.generate_auth_token(user['user_id'])
    token = Token(user['user_id'], auth_token)
    saved = __save_token(token)
    if not saved:
        raise InternalServerError(description='Failed generate reflesh token')

    return ApiResponse(200, data={'auth_token': auth_token})


def __save_token(token):
    mapper = AuthMapper()
    return mapper.save_token(token)


def __get_token(user_id):
    mapper = AuthMapper()
    access_date = datetime.now().date()
    return mapper.find_logged_in_user_token(user_id, access_date)
