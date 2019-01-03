from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.item import Item
from app.model.mapper.item_mapper import ItemMapper


bp = Blueprint('item', __name__, url_prefix='/api/items')


@bp.route('/', methods=['GET'])
def index():
    if request.args is None:
        category_id = 1
    else:
        category_id = request.args.get('category_id')
    items = Item.find_by(category_id)
    res = ResponseBody()
    res.set_success_response(200, {'items': items})
    return res


@bp.route('/', methods=['POST'])
def add():
    res = ResponseBody()

    if request.json is None:
        res.set_fail_response(400)
        return res

    item = Item(**request.json)

    if not item.is_valid():
        res.set_fail_response(400, item.validation_errors)
        return res

    mapper = ItemMapper()
    saved = mapper.add(item)

    if saved:
        res.set_success_response(201)
    else:
        res.set_fail_response(409)
    return res


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    res = ResponseBody()

    if request.json is None:
        res.set_fail_response(400)
        return res

    item = Item(**request.json)
    if not item.is_valid():
        res.set_fail_response(400, item.validation_errors)
        return res

    mapper = ItemMapper()
    saved = mapper.add(item)

    if saved:
        res.set_success_response(200, message='更新しました')
    else:
        res.set_fail_response(409)
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    res = ResponseBody()
    mapper = ItemMapper()
    deleted = mapper.delete(id)

    if deleted:
        res.set_success_response(204)
    else:
        res.set_success_response(404)
    return res
