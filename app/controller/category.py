from flask import jsonify, request, Blueprint
from app.model.category import Category
from app.model.mapper.category_mapper import CategoryMapper
from app.model.response import ResponseBodyCreator


bp = Blueprint('category', __name__, url_prefix='/api/categories')


@bp.route('/', methods=['GET'])
def index():
    body_createor = ResponseBodyCreator()
    body = body_createor.ok({'categories': Category.find_all()})
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

    category = Category(**request.json)

    if not category.is_valid():
        body = body_creator.bad_request(category.validation_errors)
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    mapper = CategoryMapper()
    saved = mapper.add(category)

    if saved:
        body = body_creator.created(request.json)
    elif not saved and category.validation_errors:
        body = body_creator.bad_request(category.validation_errors)

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

    category = Category(id, **request.json)

    if not category.is_valid():
        body = body_creator.bad_request(category.validation_errors)
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    mapper = CategoryMapper()
    saved = mapper.edit(category)

    if saved:
        body = body_creator.ok({'data': request.json}, '更新しました')
    elif not saved and category.validation_errors:
        body = body_creator.conflict(category.validation_errors)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    mapper = CategoryMapper()
    deleted = mapper.delete(id)
    body_creator = ResponseBodyCreator()

    if deleted:
        body = body_creator.no_content()
    else:
        body = body_creator.not_found()

    res = jsonify(body)
    res.status_code = body['status_code']
    return res
