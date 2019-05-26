from flask import request, Blueprint
from werkzeug.exceptions import BadRequest, Conflict, NotFound
from app.libs.api_response import ApiResponse
from app.model.user import User, UserSearchOption
from app.model.mapper.user_mapper import UserMapper


bp = Blueprint('user', __name__, url_prefix='/api/users')


@bp.route('/', methods=['GET'])
def index():
    option = UserSearchOption()
    if request.args is not None:
        option.q = request.args.get('q', type=str)

    mapper = UserMapper()
    users = mapper.find(option)

    return ApiResponse(200, data={'users': users})


@bp.route('/', methods=['POST'])
def add():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()

    user = User(**request_data)
    if not user.is_valid():
        raise BadRequest(
            description='保存エラー。エラー内容を確認してください。',
            response=user.validation_errors
        )

    mapper = UserMapper()
    saved = mapper.save(user)
    if not saved:
        raise Conflict()

    return ApiResponse(201, message='保存しました')


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()

    user = User(**request_data)
    if not user.is_valid():
        raise BadRequest(
            description='保存エラー。エラー内容を確認してください。',
            response=user.validation_errors
        )

    mapper = UserMapper()
    saved = mapper.save(user)
    if not saved:
        raise Conflict()

    return ApiResponse(200, message='更新しました')


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    mapper = UserMapper()
    deleted = mapper.delete(id)

    if not deleted:
        raise NotFound()

    return ApiResponse(204, '削除しました')
