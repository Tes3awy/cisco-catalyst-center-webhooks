# -*- coding: utf-8 -*-
from flask import Flask

from app.extensions import basic_auth, db, moment, socketio
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")
    app.config.from_object(config_class)

    db.init_app(app)
    moment.init_app(app)
    socketio.init_app(app)
    basic_auth.init_app(app)

    from app import models

    with app.app_context():
        db.create_all()

    from app.main import bp as main_bp

    app.register_blueprint(main_bp)

    from app.webhook import bp as webhook_bp

    app.register_blueprint(webhook_bp, url_prefix="/api/v1")

    from app.error import bp as error_bp

    app.register_blueprint(error_bp)

    return app
