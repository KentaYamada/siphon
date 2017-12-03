# -*- coding: utf-8 -*-


from flask import jsonify, request
from siphon import app
from siphon.models.monthly_item import MonthlyItem
from siphon.models.category import Category
from siphon.models.product import Product
from siphon.models.tax import Tax


def toDimentionArray(arr, row, col):
    res = []
    offset = 0

    for i in range(0, row):
        res.append(arr[offset:col+offset])
        offset += col
    return res


def get_dummy():
    res = []
    product_id = 1

    for i in range(1, 11):
        category = {
            "id": i,
            "name": "Category{0}".format(i),
            "products": []
        }

        for j in range(1, 31):
            category['products'].append({
                "id": product_id,
                "name": "Product{0}".format(product_id),
                "price": j * 100
            })
            product_id += 1
        category['products'] = toDimentionArray(category['products'], 10, 3)
        res.append(category)

    res = toDimentionArray(res, 2, 5)
    return res


@app.route("/api/sales", methods=["GET"])
def init():
    return jsonify({"categories": get_dummy()})


@app.route("/api/sales", methods=["POST"])
def save_sales():
    print(request.json)
    return jsonify({'result': True, 'message': '登録しました。'})


@app.route("/api/sales/<string:month>/monthly", methods=["GET"])
def find_monthly_items(month):
    return jsonify({"items": MonthlyItem.find_by()})


@app.route("/api/categories", methods=["GET"])
def find_all_categories():
    categories = Category.find_all_categories()
    return jsonify({"categories": categories})


@app.route("/api/categories", methods=["POST"])
def save_category():
    print(request.json)
    return jsonify({'result': True, 'message': '登録しました。'})


@app.route("/api/categories/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    print(request.json)
    return jsonify({'result': True, 'message': '更新しました。'})


@app.route("/api/categories/<int:id>", methods=["DELETE"])
def delete_category(id):
    print(request.json)
    return jsonify({'result': True, 'message': '更新しました。'})


@app.route("/api/products/<int:category_id>")
def find_by_products(category_id=1):
    products = Product.find_by_products(category_id)
    return jsonify({"products": products})


@app.route("/api/tax", methods=["GET"])
def find_tax():
    tax = Tax.find_tax()
    return jsonify({'tax': {'rate': tax.rate, 'tax_type': tax.tax_type}})


@app.route("/api/tax", methods=["POST"])
def save_tax():
    print(request.json)
    return jsonify({'result': True, 'message': ''})
