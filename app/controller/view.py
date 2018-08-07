from flask import render_template, Blueprint


bp = Blueprint('view', __name__, template_folder='templates')


@bp.route('/categories', methods=['GET'])
def categories():
    return render_template('category_list.html')


@bp.route('/items', methods=['GET'])
def items():
    return render_template('item_list.html')


@bp.route('/users', methods=['GET'])
def users():
    return render_template('user_list.html')
