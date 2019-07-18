from flask import request, Blueprint
from werkzeug.exceptions import BadRequest
from app.libs.api_response import ApiResponse
from app.libs.jwt_handler import api_required
from app.libs.datetime_formatter import format_date, format_time
from app.model.daily_sales import DailySalesSearchOption
from app.model.mapper.sales_mapper import SalesMapper
from app.model.mapper.sales_item_mapper import SalesItemMapper


bp = Blueprint('daily_sales', __name__, url_prefix='/api/sales/daily')


@bp.route('/', methods=['GET'])
@api_required
def index():
    request_query = request.args
    if request_query is None:
        raise BadRequest()

    sales_date = format_date(request_query.get('sales_date', type=str))

    start_time = None
    if request_query.get('time_from', type=str):
        start_time = format_time(request_query.get('time_from', type=str))

    end_time = None
    if request_query.get('time_to', type=str):
        end_time = format_time(request_query.get('time_to', type=str))

    option = DailySalesSearchOption(
        sales_date=sales_date,
        start_time=start_time,
        end_time=end_time
    )
    mapper = SalesMapper()

    daily_sales = mapper.find_daily_sales(option)
    if len(daily_sales) > 0:
        sales_ids = [s['id'] for s in daily_sales]
        item_mapper = SalesItemMapper()
        sales_items = item_mapper.find_daily_sales_items(sales_ids)
        for s in daily_sales:
            items = []
            for item in sales_items:
                if item['sales_id'] == s['id']:
                    items.append(item)
            s['items'] = items

    return ApiResponse(200, data={'daily_sales': daily_sales})
