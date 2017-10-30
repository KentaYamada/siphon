# -*- coding: utf-8 -*-


from flask import jsonify
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


@app.route("/api/sales/init", methods=["GET"])
def init():
    # ToDo: If create database, get data from database.
    return jsonify({"categories": get_dummy()})


@app.route("/api/sales/items/monthly/<string:month>", methods=["GET"])
def find_monthly_items(month):
    return jsonify({"items": MonthlyItem.find_by()})


@app.route("/api/categories/find/all")
def find_all_categories():
    categories = Category.find_all_categories()
    return jsonify({"categories": categories})


@app.route("/api/products/find/<int:category_id>")
def find_by_products(category_id=1):
    products = Product.find_by_products(category_id)
    return jsonify({"products": products})


@app.route("/api/tax/find")
def find_tax():
    tax = Tax.find_tax()
    return jsonify({'tax': {'rate': tax.rate, 'tax_type': tax.tax_type}})
