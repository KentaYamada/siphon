from datetime import datetime
from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.daily_sales import DailySalesSearchOption
from app.model.mapper.sales_mapper import SalesMapper
from app.model.mapper.sales_item_mapper import SalesItemMapper


bp = Blueprint('daily_sales', __name__, url_prefix='/api/sales/daily')


@bp.route('/', methods=['GET'])
def index():
    res = ResponseBody()

    if request.args is None:
        res.set_fail_response(400)
        return res

    sales_date = datetime.strptime(
        request.args.get('sales_date', type=str),
        '%Y-%m-%d'
    ).date()

    start_time = None
    if request.args.get('time_from', type=str):
        start_time = datetime.strptime(
            request.args.get('time_from'),
            '%H:%M:%S'
        ).time()
    end_time = None
    if request.args.get('time_to', type=str):
        end_time = datetime.strptime(
            request.args.get('time_to'),
            '%H:%M:%S'
        ).time()
    option = DailySalesSearchOption(
        sales_date=sales_date,
        start_time=start_time,
        end_time=end_time
    )
    mapper = SalesMapper()
    try:
        daily_sales = mapper.find_daily_sales(option)
        if len(daily_sales) > 0:
            sales_ids = [s['id'] for s in daily_sales]
            item_mapper = SalesItemMapper()
            sales_items = item_mapper.find_daily_sales_items(sales_ids)
            for s in daily_sales:
                s['items'] = [item for item in sales_items if item['sales_id'] == s['id']]
        res.set_success_response(200, {'daily_sales': daily_sales})
    except Exception as e:
        # todo: logging
        print(e)
        res.set_fail_response(500)
    return res


def str2time(value):
    pass
