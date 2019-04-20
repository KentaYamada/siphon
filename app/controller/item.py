from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.item import Item, ItemSearchOption
from app.model.mapper.item_mapper import ItemMapper


bp = Blueprint('item', __name__, url_prefix='/api/items')


@bp.route('/', methods=['GET'])
def index():
    option = ItemSearchOption()
    if request.args is not None:
        option.category_id = request.args.get('category_id', type=int)
        option.q = request.args.get('q', type=str)
    mapper = ItemMapper()
    items = mapper.find(option)
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
        res.set_fail_response(
            400,
            item.validation_errors,
            '保存エラー。エラー内容を確認してください。')
        return res

    mapper = ItemMapper()
    saved = mapper.save(item)

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
        res.set_fail_response(
            400,
            item.validation_errors,
            '保存エラー。エラー内容を確認してください。')
        return res

    mapper = ItemMapper()
    saved = mapper.save(item)

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
