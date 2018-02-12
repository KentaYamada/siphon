# -*- coding: utf-8 -*-
from flask import Blueprint, render_template


view_bp = Blueprint('view', __name__, template_folder='templates')


@view_bp.route('/testview', methods=['GET'])
def test_view():
    return render_template('test_view.html')


@view_bp.route("/sales", methods=["GET"])
def register():
    return render_template("register.html")


@view_bp.route("/sales/monthly", methods=["GET"])
def monthly_sales():
    return render_template("monthly_sales.html")


@view_bp.route("/categories", methods=["GET"])
def category():
    return render_template("category.html")


@view_bp.route("/products", methods=["GET"])
def product():
    return render_template("product.html")


@view_bp.route("/tax", methods=["GET"])
def tax():
    return render_template("tax.html")


@view_bp.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@view_bp.route("/users", methods=["GET"])
def user():
    return render_template("user.html")
