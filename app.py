# coding: utf-8

from flask import Flask


def create_app():
    from yoggsaron.models import init_db
    app = Flask(__name__)
    init_db(app)
