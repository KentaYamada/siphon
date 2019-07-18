from flask import request, Blueprint
from werkzeug.exceptions import (
    BadRequest,
    Conflict,
    NotFound
)
from app.libs.api_response import ApiResponse
from app.libs.jwt_handler import api_required
from app.model.category import (
    Category,
    CategorySearchOption
)
from app.model.mapper.category_mapper import CategoryMapper


bp = Blueprint('category', __name__, url_prefix='/api/categories')


@bp.route('/', methods=['GET'])
@api_required
def index():
    option = CategorySearchOption()
    if request.args is not None:
        option = CategorySearchOption(
            q=request.args.get('q', type=str)
        )

    mapper = CategoryMapper()
    categories = mapper.find(option)

    return ApiResponse(200, data={'categories': categories})


@bp.route('/', methods=['POST'])
@api_required
def add():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()

    category = Category(**request.json)
    if not category.is_valid():
        raise BadRequest(
            description='保存エラー。エラー内容を確認してください。',
            response=category.validation_errors
        )

    mapper = CategoryMapper()
    if mapper.is_upper_limit():
        raise BadRequest(description='商品カテゴリの登録数は10件までです')

    saved = mapper.save(category)
    if not saved:
        raise Conflict()

    return ApiResponse(201, message='保存しました')


@bp.route('/<int:id>', methods=['PUT'])
@api_required
def edit(id):
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()

    category = Category(**request.json)
    if not category.is_valid():
        raise BadRequest(
            description='保存エラー。エラー内容を確認してください。',
            response=category.validation_errors
        )

    mapper = CategoryMapper()
    saved = mapper.save(category)
    if not saved:
        raise Conflict()

    return ApiResponse(200, message='更新しました')


@bp.route('/<int:id>', methods=['DELETE'])
@api_required
def delete(id):
    mapper = CategoryMapper()
    deleted = mapper.delete(id)
    if not deleted:
        raise NotFound(description='リクエストデータはすでに削除されたか、または存在しません。')

    return ApiResponse(204, '削除しました')
