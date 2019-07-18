from flask import request, Blueprint
from werkzeug.exceptions import (
    BadRequest,
    Conflict
)
from app.libs.api_response import ApiResponse
from app.libs.jwt_handler import api_required
from app.model.tax_rate import TaxRate
from app.model.mapper.tax_rate_mapper import TaxRateMapper


bp = Blueprint('tax_rate', __name__, url_prefix='/api/tax_rates')


@bp.route('/', methods=['GET'])
@api_required
def index():
    mapper = TaxRateMapper()
    tax_rate = mapper.find_current_tax_rate()
    return ApiResponse(200, data={'tax_rate': tax_rate})


@bp.route('/', methods=['POST'])
@api_required
def add():
    data = request.get_json()
    if data is None:
        raise BadRequest()

    tax_rate = TaxRate(**data)
    if not tax_rate.is_valid():
        raise BadRequest(
            description='保存エラー。エラー内容を確認してください。',
            response=tax_rate.validation_errors
        )

    mapper = TaxRateMapper()
    saved = mapper.save(tax_rate)
    if not saved:
        raise Conflict(description='保存エラー。データが重複しています。')

    return ApiResponse(200, message='保存しました。')
