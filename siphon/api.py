# -*- coding: utf-8 -*-


from flask import jsonify
from siphon import app


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

def dummy_products(category_id):
    products = []
    product_id = 1
    for i in range(1, 11):
        for j in range(1, 31):
            product = {
                'id': product_id,
                'category_id': i,
                'name': 'Product{0}'.format(product_id),
                'price': j * 100
            }
            products.append(product)
            product_id += 1
    return [row for row in products if row['category_id'] == category_id]


@app.route("/api/sales/init", methods=["GET"])
def init():
    # ToDo: If create database, get data from database.
    return jsonify({"categories": get_dummy()})


@app.route("/api/categories/find/all")
def find_all_categories():
    categories = [{'id': x, 'name': 'Category{0}'.format(x)} for x in range(1, 11)]
    return jsonify({"categories": categories})


@app.route("/api/products/find/<int:category_id>")
def find_by_products(category_id=1):
    products = dummy_products(category_id)
    return jsonify({"products": products})


@app.route("/api/tax/find")
def find_tax():
    return jsonify({'tax': {'rate': 8, 'tax_type': 'out'}})
