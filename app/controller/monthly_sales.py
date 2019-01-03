from flask import Blueprint
from app.controller.response import ResponseBody
from app.model.monthly_sales import MonthlySales


bp = Blueprint('monthly_sales', __name__)


@bp.route('/api/sales/monthly/<int:year>/<int:month>', methods=['GET'])
def index(year, month):
    res = ResponseBody()
    monthly_sales = MonthlySales().findBy(year, month)
    res.set_success_response(200, {'monthly_sales': monthly_sales})
    return res
