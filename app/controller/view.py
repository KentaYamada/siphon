from flask import render_template, Blueprint


bp = Blueprint('view', __name__, template_folder='templates')


@bp.route('/users', methods=['GET'])
def users():
    return render_template('user_list.html')
