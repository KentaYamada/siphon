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
    pass
