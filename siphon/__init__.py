# -*- coding: utf-8 -*-

from flask import Flask, render_template, session


app = Flask(__name__)


# @app.before_request
# def before_request():
#     is_demo_user = session.get['demo']
#     is_logged_in_user = session.get['logged_in']


# Todo: Blueprint化
import siphon.api
import siphon.views
