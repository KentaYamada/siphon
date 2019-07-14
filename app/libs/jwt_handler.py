from functools import wraps
from flask import request
from flask_jwt_extended import verify_jwt_in_request
from app.config import get_config
from app.libs.api_response import ApiResponse
from app.model.mapper.auth_mapper import AuthMapper


def api_required(func):
    """
        Flask-JWT-extended
        API custom decorator function
        See: https://flask-jwt-extended.readthedocs.io/en/latest/custom_decorators.html
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        config = get_config()
        if not config.TESTING:
            verify_jwt_in_request()
        return func(*args, **kwargs)
    return wrapper


def user_loader_handler(identity):
    """
        Flask-JWT-extended
        user_loader_callback_loader callback function
    """
    access_token = __get_request_token()
    if access_token is None:
        return None
    mapper = AuthMapper()
    user = mapper.find_logged_in_user_token(identity)
    return identity if user else None


def user_loader_error_handler(identity):
    """
        Flask-JWT-extended
        user_loader_error_loader callback function
    """
    message = 'Unauthorization. Please reflesh token.'
    data = {'refleshing': True}
    return ApiResponse(401, message=message, data=data)


def token_in_blacklist_handler(decoded_jwt):
    """
        Flask-JWT-extended
        user_loader_error_loader callback function
    """
    print(decoded_jwt)
    mapper = AuthMapper()
    access_token = __get_request_token()
    return mapper.has_blacklist(access_token)


def __get_request_token():
    auth = request.headers.get('Authorization', type=str)
    auth_type, access_token = auth.split(' ')
    return access_token
