from flask import jsonify, Blueprint
from app.model.monthly_sales import MonthlySales


bp = Blueprint('monthly_sales', __name__)


@bp.route('/api/sales/monthly/<int:year>/<int:month>', methods=['GET'])
def index(year, month):
    monthly_sales = MonthlySales().findBy(year, month)
    return jsonify({'monthly_sales': monthly_sales})
