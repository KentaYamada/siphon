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


@app.route("/api/sales", methods=["GET"])
def init():
    # ToDo: If create database, get data from database.
    return jsonify({"categories": get_dummy()})
