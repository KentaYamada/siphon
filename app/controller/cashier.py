from flask import jsonify, Blueprint


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
    pass
