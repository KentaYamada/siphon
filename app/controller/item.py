from flask import request, jsonify, Blueprint
from app.model.item import Item
from app.model.mapper.item_mapper import ItemMapper
from app.model.response import ResponseBodyCreator


bp = Blueprint('item', __name__, url_prefix='/api/items')


@bp.route('/', methods=['GET'])
def index():
    if request.args is None:
        category_id = 1
    else:
        category_id = request.args.get('category_id')
    items = Item.find_by(category_id)
    body_creator = ResponseBodyCreator()
    body = body_creator.ok({'items': items}, message='データ取得成功')
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

    item = Item(**request.json)
    if not item.is_valid():
        body = body_creator.bad_request(item.validation_errors)
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    mapper = ItemMapper()
    saved = mapper.add(item)

    if saved:
        body = body_creator.created(request.json)
    elif not saved and item.errors:
        body = body_creator.bad_request(item.errors)

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

    item = Item(**request.json)
    if not item.is_valid():
        body = body_creator.bad_request(item.validation_errors)
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    mapper = ItemMapper()
    saved = mapper.add(item)

    if saved:
        body = body_creator.ok(request.json)
    elif not saved and len(item.errors) > 0:
        body = body_creator.conflict(item.errors)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    mapper = ItemMapper()
    deleted = mapper.delete(id)
    body_creator = ResponseBodyCreator()

    if deleted:
        body = body_creator.no_content()
    else:
        body = body_creator.not_found()

    res = jsonify(body)
    res.status_code = body['status_code']
    return res
