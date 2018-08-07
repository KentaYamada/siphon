from flask import render_template, Blueprint


NAVIGATION_MENUS = [
    {
        'name': '売上',
        'icon': 'glyphicon-usd',
        'submenu': [
            {
                'name': '売上登録',
                'url': 'sales',
                'icon': 'glyphicon-shopping-cart'
            },
            {
                'name': '今日の売上',
                'url': 'sales/daily',
                'icon': 'glyphicon-list'
            },
            {
                'name': '今月の売上',
                'url': 'sales/monthly',
                'icon': 'glyphicon-calendar'
            }
        ]
    },
    {
        'name': '設定',
        'icon': 'glyphicon-cog',
        'submenu': [
            {
                'name': '商品カテゴリ',
                'url': 'categories',
                'icon': 'glyphicon-shopping-cart'
            },
            {
                'name': '商品',
                'url': 'items',
                'icon': 'glyphicon-barcode'
            },
            {
                'name': 'ユーザー',
                'url': 'users',
                'icon': 'glyphicon-user'
            }
        ]
    }
]


bp = Blueprint('view', __name__, template_folder='templates')


@bp.route('/categories', methods=['GET'])
def categories():
    return render_template('category_list.html', menu=NAVIGATION_MENUS)


@bp.route('/items', methods=['GET'])
def items():
    return render_template('item_list.html', menu=NAVIGATION_MENUS)


@bp.route('/users', methods=['GET'])
def users():
    return render_template('user_list.html', menu=NAVIGATION_MENUS)
