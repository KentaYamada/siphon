from flask import jsonify, Blueprint
from app.model.category import Category


bp = Blueprint('category', __name__, url_prefix='/api/categories')


@bp.route('/', methods=['GET'])
def index():
    categories = Category().find_all()
    return jsonify({'categories': categories})


@bp.route('/', methods=['POST'])
def add():
    pass


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    pass


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    res = {
        'status': None,
        'message': '',
        'errors': []
    }
    if id is None:
        res['status'] = 404
        res['message'] = 'id is empty'
    else:
        res['status'] = 204
        res['message'] = 'deleted'
    return jsonify(res)
