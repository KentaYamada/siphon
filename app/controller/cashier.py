from datetime import datetime
from flask import request, Blueprint
from werkzeug.exceptions import BadRequest, Conflict
from app.libs.api_response import ApiResponse
from app.libs.jwt_handler import api_required
from app.model.sales import Sales
from app.model.sales_item import SalesItem
from app.model.category import CategorySearchOption
from app.model.item import ItemSearchOption
from app.model.mapper.category_mapper import CategoryMapper
from app.model.mapper.item_mapper import ItemMapper
from app.model.mapper.sales_mapper import SalesMapper
from app.model.mapper.tax_rate_mapper import TaxRateMapper


bp = Blueprint('cashier', __name__, url_prefix='/api/cashier')


@bp.route('/', methods=['GET'])
@api_required
def index():
    categories = _get_categories()
    items = _get_items(categories)
    tax_rate = _get_tax_rate()

    for category in categories:
        data = [i for i in items if category['id'] == i['category_id']]
        category['items'] = data

    data = {
        'categories': categories,
        'tax_rate': tax_rate
    }
    return ApiResponse(200, data=data)


@bp.route('/', methods=['POST'])
@api_required
def add():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest()
    if request_data['items'] is None or len(request_data['items']) < 1:
        raise BadRequest(description='売上明細データがセットされていません')

    items = []
    for i, item in enumerate(request_data['items'], 1):
        items.append(SalesItem(item_no=i, **item))
    del request.json['items']
    now_date = datetime.now().date()
    now_time = datetime.now().time()
    sales = Sales(
        None,
        sales_date=now_date,
        sales_time=now_time,
        items=items,
        **request.json
    )

    if not sales.is_valid():
        raise BadRequest(
            description='保存エラー。エラー内容を確認してください。',
            response=sales.validation_errors
        )

    mapper = SalesMapper()
    saved = mapper.add(sales)
    if not saved:
        raise Conflict()

    return ApiResponse(201, message='保存しました')


def _get_categories():
    option = CategorySearchOption()
    mapper = CategoryMapper()
    rows = mapper.find(option)
    # 登録件数が10件未満の場合は、空データで埋め合わせ
    unregist_count = CategoryMapper.MAX_ADDABLE_ROW - len(rows)
    for i in range(0, unregist_count):
        rows.append({'id': None, 'name': ''})
    return rows


def _get_items(categories):
    category_ids = [c['id'] for c in categories]
    option = ItemSearchOption(
        category_ids=category_ids
    )
    mapper = ItemMapper()
    rows = mapper.find_by_category_ids(option)
    items = []
    # 登録済みカテゴリにひもづく商品がなければ、無効なカテゴリとする
    for c in categories:
        registered_items = [r for r in rows if c['id'] == r['category_id']]
        if len(registered_items) > 0:
            c['disabled'] = False
            items += registered_items
        else:
            c['disabled'] = True
    return items


def _get_tax_rate():
    mapper = TaxRateMapper()
    data = mapper.find_current_tax_rate()
    if data is not None:
        del data['start_date']
    return data
