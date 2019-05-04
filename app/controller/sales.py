from flask import request, Blueprint
from app.controller.response import ResponseBody
from app.model.mapper.sales_mapper import SalesMapper


bp = Blueprint('sales', __name__, url_prefix='/api/sales')


@bp.route('/cancel', methods=['POST'])
def cancel():
    res = ResponseBody()
    if request.json is None:
        res.set_fail_response(400)
        return res
    sales_id = request.json['params']['sales_id']
    mapper = SalesMapper()
    try:
        canceled = mapper.cancel(sales_id)
        res.set_success_response(201)
    except Exception as e:
        # todo: logging
        print(e)
        canceled = False
    if canceled:
        res.set_success_response(201)
    else:
        res.set_fail_response(409)
    return res
