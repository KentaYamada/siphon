from datetime import datetime
from calendar import monthrange
from flask import Blueprint
from app.controller.response import ResponseBody
from app.model.sales_item import PopularSalesItemSearchOption
from app.model.mapper.sales_mapper import SalesMapper
from app.model.mapper.sales_item_mapper import SalesItemMapper


bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')


@bp.route('/<int:year>/<int:month>', methods=['GET'])
def index(year, month):
    body = ResponseBody()
    try:
        monthly_sales = __get_monthly_sales(year, month)
        items = __get_popular_items(year, month)
        body.set_success_response(
            200,
            {'monthly_sales': monthly_sales, 'popular_items': items}
        )
    except Exception as e:
        # todo: logging
        print(e)
        body.set_fail_response(500)
    return body


def __get_monthly_sales(year, month):
    return []


def __get_popular_items(year, month):
    # 月末/月初
    _, last = monthrange(year, month)
    option = PopularSalesItemSearchOption(
        start_date=datetime(year, month, 1).date(),
        end_date=datetime(year, month, last).date()
    )
    mapper = SalesItemMapper()
    return mapper.find_popular_items(option)
