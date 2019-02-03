from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.mapper.sales_mapper import SalesMapper
from app.model.mapper.sales_item_mapper import SalesItemMapper


bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')


@bp.route('/<int:year>/<int:month>', methods=['GET'])
def index(year, month):
    res = ResponseBody()
    sales_mapper = SalesMapper()
    item_mapper = SalesItemMapper()

    try:
        monthly_sales = sales_mapper.find_monthly_sales(year, month)
        popular_items = item_mapper.find_popular_items([1, 2])
        data = {
            'monthly_sales': monthly_sales,
            'popular_items': popular_items
        }
        res.set_success_response(200, data)
    except Exception as e:
        # todo logging
        print(e)
        res.set_fail_response(500, message=e)
    return res
