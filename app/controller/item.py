from flask import request, jsonify, Blueprint
from app.model.item import Item
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

    item = Item(
        None,
        request.json['category_id'],
        request.json['name'],
        request.json['unit_price'])
    saved = item.save()

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

    item = Item(
        id,
        request.json['category_id'],
        request.json['name'],
        request.json['unit_price'])
    saved = item.save()

    if saved:
        body = body_creator.ok(request.json)
    elif not saved and len(item.errors) > 0:
        body = body_creator.conflict(item.errors)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    item = Item(id)
    deleted = item.delete()
    body_creator = ResponseBodyCreator()

    if deleted:
        body = body_creator.no_content()
    else:
        body = body_creator.not_found()

    res = jsonify(body)
    res.status_code = body['status_code']
    return res
