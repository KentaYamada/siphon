from datetime import datetime
from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.sales import Sales
from app.model.sales_item import SalesItem
from app.model.mapper.sales_mapper import SalesMapper


bp = Blueprint('cashier', __name__, url_prefix='/api/cashier')


def to_dimention_array(arr, row, col):
    """ 一次元配列から二次元配列へ変換 """
    res = []
    offset = 0

    for i in range(0, row):
        res.append(arr[offset:col+offset])
        offset += col
    return res


def generatePanel():
    """ 商品選択パネルダミーデータ生成 """
    data = {'categories': []}
    item_id = 1
    for i in range(1, 11):
        category = {
            'id': i,
            'name': 'Category{}'.format(i),
            'items': []
        }

        for j in range(1, 31):
            category['items'].append({
                "id": item_id,
                "name": "Item{}".format(item_id),
                "unit_price": j * 100
            })
            item_id += 1
        category['items'] = to_dimention_array(category['items'], 10, 3)
        data['categories'].append(category)
    data['categories'] = to_dimention_array(data['categories'], 2, 5)
    return data


@bp.route('/', methods=['GET'])
def index():
    res = ResponseBody()
    data = generatePanel()
    res.set_success_response(200, data)
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

    items = [SalesItem(None, None, i, **item)
             for i, item in enumerate(request.json['items'], 1)]
    del request.json['items']
    now_date = datetime.now().date()
    now_time = datetime.now().time()
    sales = Sales(None, sales_date=now_date, sales_time=now_time, items=items, **request.json)

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
