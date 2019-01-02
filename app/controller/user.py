from flask import jsonify, request, Blueprint
from app.model.user import User
from app.model.mapper.user_mapper import UserMapper
from app.model.response import ResponseBodyCreator


bp = Blueprint('user', __name__, url_prefix='/api/users')


@bp.route('/', methods=['GET'])
def index():
    body_createor = ResponseBodyCreator()
    body = body_createor.ok(User.find_by(''))
    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/', methods=['POST'])
def add():
    body_createor = ResponseBodyCreator()

    if request.json is None:
        body = body_createor.bad_request()
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    user = User(None, **request.json)
    if not user.is_valid():
        body = body_createor.bad_request(user.validation_errors)
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    mapper = UserMapper()
    saved = mapper.add(user)

    if saved:
        body = body_createor.created(request.json)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    body_createor = ResponseBodyCreator()
    user = User(id, **request.json)

    if not user.is_valid():
        body = body_createor.bad_request(user.validation_errors)
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    mapper = UserMapper()
    saved = mapper.edit(user)

    if saved:
        body = body_createor.ok(request.json)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    mapper = UserMapper()
    deleted = mapper.delete(id)
    body_createor = ResponseBodyCreator()

    if deleted:
        body = body_createor.no_content('delete successfuly')
    else:
        body = body_createor.not_found('resource not found')

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/authoricate', methods=['POST'])
def authoricate():
    body_createor = ResponseBodyCreator()

    if request.json is None:
        body = body_createor.bad_request(
            ['空のリクエストデータです']
        )
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    mapper = UserMapper()
    can_login = mapper.authoricate(**request.json)

    if can_login:
        body = body_createor.ok(None, 'authorication successfuly')
    else:
        body = body_createor.unauthorized('failed authorication')

    res = jsonify(body)
    res.status_code = body['status_code']
    return res
