from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.category import Category
from app.model.mapper.category_mapper import CategoryMapper


bp = Blueprint('category', __name__, url_prefix='/api/categories')


@bp.route('/', methods=['GET'])
def index():
    categories = Category.find_all()
    res = ResponseBody()
    res.set_success_response(200, categories)
    return res


@bp.route('/', methods=['POST'])
def add():
    res = ResponseBody()

    if request.json is None:
        res.set_fail_response(400)
        return res

    category = Category(**request.json)

    if not category.is_valid():
        res.set_fail_response(400, category.validation_errors)
        return res

    mapper = CategoryMapper()
    saved = mapper.add(category)

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

    category = Category(id, **request.json)

    if not category.is_valid():
        res.set_fail_response(400)
        return res

    mapper = CategoryMapper()
    saved = mapper.edit(category)

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
