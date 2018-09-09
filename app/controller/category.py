from flask import jsonify, request, Blueprint
from app.model.category import Category
from app.model.response import ResponseBodyCreator


bp = Blueprint('category', __name__, url_prefix='/api/categories')


@bp.route('/', methods=['GET'])
def index():
    body_createor = ResponseBodyCreator()
    body = body_createor.ok(Category.find_all())
    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/', methods=['POST'])
def add():
    body_creator = ResponseBodyCreator()

    if request.json is None:
        body = body_creator.bad_request(None)
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    category = Category(
        None,
        request.json['name'])
    saved = category.save()

    if saved:
        body = body_creator.created(request.json)
    elif not saved and category.errors:
        body = body_creator.bad_request(category.errors)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    body_creator = ResponseBodyCreator()

    if request.json is None:
        body = body_creator.bad_request()
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    category = Category(
        id,
        request.json['name'])
    saved = category.save()

    if saved:
        body = body_creator.ok(request.json)
    elif not saved and len(category.errors) > 0:
        body = body_creator.conflict(category.errors)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    category = Category(id)
    deleted = category.delete()
    body_creator = ResponseBodyCreator()

    if deleted:
        body = body_creator.no_content()
    else:
        body = body_creator.not_found()

    res = jsonify(body)
    res.status_code = body['status_code']
    return res
