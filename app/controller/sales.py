from flask import request, Blueprint
from werkzeug.exceptions import BadRequest, Conflict, NotFound
from app.libs.api_response import ApiResponse
from app.model.mapper.sales_mapper import SalesMapper


bp = Blueprint('sales', __name__, url_prefix='/api/sales')


@bp.route('/cancel', methods=['POST'])
def cancel():
    request_data = request.get_json()
    if request_data is None:
        raise BadRequest(description='売上IDをセットしてください')

    # todo: 売上データ存在チェック
    # if sales_data is None:
    #     raise NotFound(description='取消対象の売上データが見つかりませんでした')

    mapper = SalesMapper()
    canceled = mapper.cancel(request_data['params']['sales_id'])
    if not canceled:
        raise Conflict()

    return ApiResponse(201, message='売上キャンセルしました')
