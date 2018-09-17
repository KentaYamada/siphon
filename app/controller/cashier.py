from datetime import datetime
from flask import jsonify, request, Blueprint
from app.model.sales import Sales
from app.model.sales_item import SalesItem
from app.model.response import ResponseBodyCreator


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
    data = generatePanel()
    return jsonify(data)


@bp.route('/', methods=['POST'])
def add():
    body_creator = ResponseBodyCreator()

    if request.json is None:
        body = body_creator.bad_request(None)
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    if request.json['items'] is None or len(request.json['items']) < 1:
        body = body_creator.bad_request('売上明細データがセットされていません')
        res = jsonify(body)
        res.status_code = body['status_code']
        return res

    now_date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    items = []
    for i, item in enumerate(request.json['items']):
        items.append(SalesItem(
            None,
            None,
            now_date,
            i + 1,
            item['item_name'],
            item['unit_price'],
            item['quantity'],
            item['subtotal']))
    sales = Sales(
        None,
        now_date,
        request.json['total_price'],
        request.json['discount_price'],
        request.json['discount_rate'],
        request.json['inclusive_tax'],
        request.json['exclusive_tax'],
        request.json['deposit'],
        items)
    saved = sales.save()

    if saved:
        body = body_creator.created(None)
    elif not saved and sales.errors:
        body = body_creator.bad_request(sales.errors)

    res = jsonify(body)
    res.status_code = body['status_code']
    return res
