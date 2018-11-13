from flask import jsonify, request, Blueprint
from app.model.user import User
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

    user = User(
        None,
        request.json['name'],
        request.json['nickname'],
        request.json['email'],
        request.json['password'])
    saved = user.save()

    if saved:
        body = body_createor.created(request.json)
    elif not user.is_valid():
        body = body_createor.bad_request(user.validation_errors)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    body_createor = ResponseBodyCreator()
    user = User(
        id,
        request.json['name'],
        request.json['nickname'],
        request.json['email'],
        request.json['password'])
    saved = user.save()

    if saved:
        body = body_createor.ok(request.json)
    elif not user.is_valid():
        body = body_createor.conflict(user.validation_errors)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    user = User(id)
    deleted = user.delete()
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

    canLogin = User.authoricate(
        request.json['user_id'],
        request.json['password']
    )

    if canLogin:
        body = body_createor.ok(None, 'authorication successfuly')
    else:
        body = body_createor.unauthorized('failed authorication')

    res = jsonify(body)
    res.status_code = body['status_code']
    return res
