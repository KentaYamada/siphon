from flask import Blueprint
from app.controller.response import ResponseBody
from app.model.monthly_sales import MonthlySales
from app.model.mapper.sales_mapper import SalesMapper

bp = Blueprint('monthly_sales', __name__)


@bp.route('/api/sales/monthly/<int:year>/<int:month>', methods=['GET'])
def index(year, month):
    mapper = SalesMapper()
    monthly_sales = mapper.find_monthly_sales(year, month)
    res = ResponseBody()
    res.set_success_response(200, {'monthly_sales': monthly_sales})
    return res
