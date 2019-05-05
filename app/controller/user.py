from flask import request, Blueprint
from app.controller.response import ResponseBody
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
    res = ResponseBody()
    res.set_success_response(200, {'users': users})
    return res


@bp.route('/', methods=['POST'])
def add():
    res = ResponseBody()

    if request.json is None:
        res.set_fail_response(400)
        return res

    user = User(**request.json)

    if not user.is_valid():
        res.set_fail_response(
            400,
            user.validation_errors,
            '保存エラー。エラー内容を確認してください。'
        )
        return res

    mapper = UserMapper()
    saved = mapper.save(user)

    if saved:
        res.set_success_response(201)
    else:
        res.set_fail_response(409)
    return res


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    res = ResponseBody()
    user = User(**request.json)

    if not user.is_valid():
        res.set_fail_response(
            400,
            user.validation_errors,
            '保存エラー。エラー内容を確認してください。')
        return res

    mapper = UserMapper()
    saved = mapper.save(user)

    if saved:
        res.set_success_response(200, message='更新しました')
    else:
        res.set_fail_response(409)
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    res = ResponseBody()
    mapper = UserMapper()
    deleted = mapper.delete(id)

    if deleted:
        res.set_success_response(204)
    else:
        res.set_success_response(404)
    return res
