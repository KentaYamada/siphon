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
    body = body_creator.created(request.json)
    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:item_id>', methods=['PUT'])
def edit(item_id):
    body_creator = ResponseBodyCreator()
    if request.json is None:
        body = body_creator.bad_request()
        res = jsonify(body)
        res.status_code = body['status_code']
        return res
    body = body_creator.created(request.json)
    res = jsonify(body)
    res.status_code = body['status_code']
    return res


@bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    pass
