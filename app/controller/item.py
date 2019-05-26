from flask import request, Blueprint
from werkzeug.exceptions import BadRequest, Conflict, NotFound
from app.libs.api_response import ApiResponse
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

    return ApiResponse(200, data={'items': items})


@bp.route('/', methods=['POST'])
def add():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()

    item = Item(**request.json)
    if not item.is_valid():
        raise BadRequest(
            description='保存エラー。エラー内容を確認してください。',
            response=item.validation_errors
        )

    mapper = ItemMapper()
    saved = mapper.save(item)
    if not saved:
        raise Conflict()

    return ApiResponse(201, message='保存しました')


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()

    item = Item(**request.json)
    if not item.is_valid():
        raise BadRequest(
            description='保存エラー。エラー内容を確認してください。',
            response=item.validation_errors
        )

    mapper = ItemMapper()
    saved = mapper.save(item)
    if not saved:
        raise Conflict()

    return ApiResponse(200, message='更新しました')


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    mapper = ItemMapper()
    deleted = mapper.delete(id)
    if not deleted:
        raise NotFound()

    return ApiResponse(204, '削除しました')
