# -*- coding: utf-8 -*-
from flask import Flask
from app.controller import api, view

app = Flask(__name__)

# setup blueprints.
app.register_blueprint(api.api_bp)
app.register_blueprint(view.view_bp)
