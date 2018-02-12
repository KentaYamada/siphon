# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, request
from app.util import get_dummy
from app.model.category import Category
from app.model.product import Product
from app.model.tax import Tax

# config
api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/', methods=['GET'])
def api_index():
    res = {
        'result': True,
        'message': 'This is api test.'
    }

    return jsonify(res)


@api_bp.route("/sales", methods=["GET"])
def init():
    return jsonify({"categories": get_dummy()})


@api_bp.route("/sales", methods=["POST"])
def save_sales():
    return jsonify({'result': True, 'message': '登録しました。'})


@api_bp.route("/sales/monthly/<int:year>/<int:month>", methods=["GET"])
def find_monthly_sales(year, month):
    # デフォルトを日曜に
    calendar.setfirstweekday(calendar.SUNDAY)
    current = calendar.monthcalendar(year, month)
    res = []
    for days in current:
        week = []
        for day in days:
            week.api_bpend({'sales_date': day, 'amount': 1000})
        res.api_bpend(week)
    return jsonify({'data': res})


@api_bp.route("/sales/<string:month>/monthly", methods=["GET"])
def find_monthly_items(month):
    return jsonify({"items": MonthlyItem.find_by()})


@api_bp.route("/categories", methods=["GET"])
def find_all_categories():
    categories = Category.find_all_categories()
    return jsonify({"categories": categories})


@api_bp.route("/categories", methods=["POST"])
def save_category():
    print(request.json)
    return jsonify({'result': True, 'message': '登録しました。'})


@api_bp.route("/categories/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    print(request.json)
    return jsonify({'result': True, 'message': '更新しました。'})


@api_bp.route("/categories/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    print(request.json)
    return jsonify({'result': True, 'message': '更新しました。'})


@api_bp.route("/products/<int:category_id>")
def find_by_products(category_id=1):
    products = Product.find_by_products(category_id)
    return jsonify({"products": products})


@api_bp.route("/tax", methods=["GET"])
def find_tax():
    tax = Tax.find_tax()
    # return jsonify({'tax': {'rate': tax.rate, 'tax_type': tax.tax_type}})
    return jsonify({'tax': {'rate': tax['rate'], 'tax_type': tax['tax_type']}})


@api_bp.route("/tax", methods=["POST"])
def save_tax():
    print(request.json)
    return jsonify({'result': True, 'message': ''})
