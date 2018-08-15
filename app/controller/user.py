from flask import jsonify, url_for, Blueprint


bp = Blueprint('user', __name__, url_prefix='/api/users')


@bp.route('/authoricate', methods=['POST'])
def authoricate():
    return jsonify({
        'authoricate': True,
        'redirect_url': url_for('view.index')
    })
