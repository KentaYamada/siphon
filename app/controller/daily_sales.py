from flask import Blueprint
from app.controller.response import ResponseBody
from app.model.sales import Sales
from app.model.mapper.sales_mapper import SalesMapper
from app.model.mapper.sales_item_mapper import SalesItemMapper


bp = Blueprint('daily_sales', __name__, url_prefix='/api/daily_sales')


@bp.route('/<int:year>/<int:month>/<int:day>', methods=['GET'])
def index(year, month, day):
    sales_mapper = SalesMapper()
    res = ResponseBody()
    try:
        sales = sales_mapper.find_daily_sales()
        if sales is not None:
            sales_item_mapper = SalesItemMapper()
            sales_ids = [s.id for s in sales]
            sales_items = sales_item_mapper.find_by_sales_ids(sales_ids)
            for s in sales:
                s.items = [i for i in sales_items if s.id == i.sales_id]
        res.set_success_response(200, {'daily_sales': sales})
    except Exception as e:
        # todo: logging
        print(e)
        res.set_fail_response(500)
    return res
