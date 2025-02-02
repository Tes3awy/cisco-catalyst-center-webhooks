# -*- coding: utf-8 -*-
import base64
import os
import secrets


class Config(object):
    """Base config."""

    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex())
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_SERVER = "localhost"
    # Username for the webhook BasicAuth (Change if needed)
    BASIC_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME", "admin")
    # Password for the webhook BasicAuth (Change if needed)
    BASIC_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD", "Cisco!2345")
    BASIC_AUTH_REALM = "Login Required"
    BASIC_AUTH_FORCE = False
    # Authorization String
    BASIC_AUTH = base64.b64encode(
        f"{BASIC_AUTH_USERNAME}:{BASIC_AUTH_PASSWORD}".encode("utf-8")
    ).decode("utf-8")
    # Pagination
    PER_PAGE = 10
    MAX_PER_PAGE = 100
    # Cache-Control
    SEND_FILE_MAX_AGE_DEFAULT = 300
    PREFERRED_URL_SCHEME = "https"


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///webhook.sqlite3"


class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
