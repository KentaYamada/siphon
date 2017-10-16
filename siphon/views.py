# -*- conding: utf-8 -*-
from flask import render_template
from siphon import app


@app.route("/sales", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/category", methods=["GET"])
def category():
    return render_template("category.html")


@app.route("/product", methods=["GET"])
def product():
    return render_template("product.html")


@app.route("/tax", methods=["GET"])
def tax():
    return render_template("tax.html")

