from flask import render_template, Blueprint


NAVIGATION_MENUS = [
    {
        'name': '売上',
        'icon': 'glyphicon-usd',
        'submenu': [
            {
                'name': 'お会計',
                'url': 'view.sales',
                'icon': 'glyphicon-shopping-cart'
            },
            {
                'name': '今日の売上',
                'url': 'sales/daily',
                'icon': 'glyphicon-list'
            },
            # {
            #     'name': '今月の売上',
            #     'url': 'view.monthly_sales',
            #     'icon': 'glyphicon-calendar'
            # }
        ]
    },
    {
        'name': '設定',
        'icon': 'glyphicon-cog',
        'submenu': [
            {
                'name': '商品カテゴリ',
                'url': 'view.categories',
                'icon': 'glyphicon-shopping-cart'
            },
            {
                'name': '商品',
                'url': 'view.items',
                'icon': 'glyphicon-barcode'
            },
            {
                'name': 'ユーザー',
                'url': 'view.users',
                'icon': 'glyphicon-user'
            }
        ]
    }
]


bp = Blueprint('view', __name__, template_folder='templates')


@bp.route('/sales', methods=['GET'])
def sales():
    return render_template('sales_register.html', menu=NAVIGATION_MENUS)


@bp.route('/sales/monthly', methods=['GET'])
def monthly_sales():
    return render_template('monthly_sales.html', menu=NAVIGATION_MENUS)


@bp.route('/categories', methods=['GET'])
def categories():
    return render_template('category_list.html', menu=NAVIGATION_MENUS)


@bp.route('/items', methods=['GET'])
def items():
    return render_template('item_list.html', menu=NAVIGATION_MENUS)


@bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@bp.route('/users', methods=['GET'])
def users():
    return render_template('user_list.html', menu=NAVIGATION_MENUS)
