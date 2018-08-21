from flask import jsonify, request, Blueprint
from app.model.response import ResponseBodyCreator
from app.model.category import Category


bp = Blueprint('category', __name__, url_prefix='/api/categories')


@bp.route('/', methods=['GET'])
def index():
    categories = Category().find_all()
    body_creator = ResponseBodyCreator()
    body = body_creator.fetch_success({'categories': categories})
    response = jsonify(body)
    response.status_code = body['status_code']
    return response


@bp.route('/', methods=['POST'])
def add():
    body_creator = ResponseBodyCreator()
    if request.json is None:
        body = body_creator.bad_request()
        response = jsonify(body)
        return response
    model = Category()
    saved = model.save()
    if saved:
        body = body_creator.added({})
    else:
        errors = ()
        body = body_creator.add_failed(errors)

    response = jsonify(body)
    response.status_code = body['status_code']
    return response


@bp.route('/<int:id>', methods=['PUT'])
def edit(id):
    pass


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    pass
