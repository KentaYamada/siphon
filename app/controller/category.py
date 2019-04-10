from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.category import Category, CategorySearchOption
from app.model.item import ItemSearchOption
from app.model.mapper.category_mapper import CategoryMapper
from app.model.mapper.item_mapper import ItemMapper


bp = Blueprint('category', __name__, url_prefix='/api/categories')


@bp.route('/', methods=['GET'])
def index():
    if request.args is not None:
        option = CategorySearchOption(**request.args)
    else:
        option = CategorySearchOption()

    mapper = CategoryMapper()
    categories = mapper.find(option)

    if len(categories) > 0 and option.with_items:
        item_option = ItemSearchOption()
        item_option.category_ids = (c['id'] for c in categories)
        item_mapper = ItemMapper()
        items = item_mapper.find_items_by_category_ids(item_option)

        if items is not None:
            for c in categories:
                c.items = (item for item in items if item['category_id'] == c['id'])

    res = ResponseBody()
    res.set_success_response(200, {'categories': categories})
    return res


@bp.route('/', methods=['POST'])
def add():
    res = ResponseBody()

    if request.json is None:
        res.set_fail_response(400)
        return res

    category = Category(**request.json)

    if not category.is_valid():
        res.set_fail_response(
            400,
            category.validation_errors,
            '保存エラー。エラー内容を確認してください')
        return res

    mapper = CategoryMapper()
    saved = mapper.save(category)

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

    category = Category(**request.json)

    if not category.is_valid():
        res.set_fail_response(
            400,
            category.validation_errors,
            '保存エラー。エラー内容を確認してください。')
        return res

    mapper = CategoryMapper()
    saved = mapper.save(category)

    if saved:
        res.set_success_response(200, message='更新しました')
    else:
        res.set_fail_response(409)
    return res


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    res = ResponseBody()
    mapper = CategoryMapper()
    deleted = mapper.delete(id)

    if deleted:
        res.set_success_response(204)
    else:
        res.set_success_response(404)
    return res
