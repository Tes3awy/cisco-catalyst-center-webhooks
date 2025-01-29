# -*- coding: utf-8 -*-
import base64
import secrets


class Config(object):
    TESTING = True
    SECRET_KEY = secrets.token_hex()
    SQLALCHEMY_DATABASE_URI = "sqlite:///webhook.sqlite3"
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Username for the webhook BasicAuth (Change if needed)
    BASIC_AUTH_USERNAME = "admin"
    # Password for the webhook BasicAuth (Change if needed)
    BASIC_AUTH_PASSWORD = "Cisco!2345"
    BASIC_AUTH_FORCE = False
    BASIC_AUTH_REALM = "Cisco Catalyst Center Webhooks Authentication Required"
    # Authorization String
    BASIC_AUTH = base64.b64encode(
        f"{BASIC_AUTH_USERNAME}:{BASIC_AUTH_PASSWORD}".encode("utf-8")
    ).decode("utf-8")
