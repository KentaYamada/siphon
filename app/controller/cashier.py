from datetime import datetime
from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.sales import Sales
from app.model.sales_item import SalesItem
from app.model.category import CategorySearchOption
from app.model.item import ItemSearchOption
from app.model.mapper.category_mapper import CategoryMapper
from app.model.mapper.item_mapper import ItemMapper
from app.model.mapper.sales_mapper import SalesMapper


bp = Blueprint('cashier', __name__, url_prefix='/api/cashier')


@bp.route('/', methods=['GET'])
def index():
    categories = _get_categories()
    items = _get_items(categories)
    for category in categories:
        data = [i for i in items if category['id'] == i['category_id']]
        category['items'] = data
    # 5x2の二次元配列へ変換
    # categories = _to_dimention_array(categories, 2, 5)
    res = ResponseBody()
    res.set_success_response(200, {'categories': categories})
    return res


@bp.route('/', methods=['POST'])
def add():
    res = ResponseBody()

    if request.json is None:
        res.set_fail_response(400)
        return res

    if request.json['items'] is None or len(request.json['items']) < 1:
        res.set_fail_response(400, message='売上明細データがセットされていません')
        return res

    items = [SalesItem(item_no=i, **item) for i, item in enumerate(request.json['items'], 1)]
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
        res.set_fail_response(400, sales.validation_errors)
        return res

    mapper = SalesMapper()
    saved = mapper.add(sales)

    if saved:
        res.set_success_response(201)
    else:
        res.set_fail_response(409)
    return res


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
    # 1カテゴリあたり登録件数が30件未満の場合は、空データで埋め合わせ
    # for c in categories:
    #     registered_items = [r for r in rows if c['id'] == r['category_id']]
    #     unregist_count = ItemMapper.MAX_ADDABLE_DATA - len(registered_items)
    #     for i in range(0, unregist_count):
    #         registered_items.append({
    #             'id': None,
    #             'category_id': c['id'],
    #             'name': '',
    #             'unit_price': None
    #         })
    #     items += registered_items
    return items


def _to_dimention_array(arr, row, col):
    """ 一次元配列から二次元配列へ変換 """
    res = []
    offset = 0
    for i in range(0, row):
        res.append(arr[offset:col+offset])
        offset += col
    return res
