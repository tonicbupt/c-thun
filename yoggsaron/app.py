# coding: utf-8

import os
import yaml
from flask import Flask
from werkzeug.utils import import_string

import yoggsaron.models
from .ext import db


blueprints = []


def read_config():
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(parent_dir, 'config.yaml')
    try:
        with open(config_path, 'r') as f:
            config = yaml.load(f)
    except:
        config = {}

    mysql = config.get('mysql', {})
    mysql_config_keys = ['username', 'password', 'host', 'port', 'db']
    mysql_config = {key: mysql.get(key, '') for key in mysql_config_keys}
    r = {
        'SQLALCHEMY_DATABASE_URI': 'mysql://{username}:{password}@{host}:{port}/{db}'.format(**mysql_config),
        'SQLALCHEMY_POOL_SIZE': 100,
        'SQLALCHEMY_POOL_TIMEOUT': 10,
        'SQLALCHEMY_POOL_RECYCLE': 3600,
    }
    return r


def create_app():

    config = read_config()

    app = Flask(__name__)
    app.config.update(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    for bp in blueprints:
        import_name = '%s.views.%s:bp' % (__package__, bp)
        app.register_blueprint(import_string(import_name))

    return app
