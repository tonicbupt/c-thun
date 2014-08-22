# coding: utf-8

from flask import Flask
from werkzeug.utils import import_string

from .ext import db


blueprints = []


def create_app(config):
    import yoggsaron.models
    app = Flask(__name__)
    app.config.update(config)

    db.init_db(app)
    db.create_all()

    for bp in blueprints:
        import_name = '%s.views.%s:bp' % (__package__, bp)
        app.register_blueprint(import_string(import_name))

    return app
