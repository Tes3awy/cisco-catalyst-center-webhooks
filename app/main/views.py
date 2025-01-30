# -*- coding: utf-8 -*-
from http import HTTPStatus

import sqlalchemy as sa
from flask import current_app, jsonify, render_template, request

from app import db
from app.main import bp
from app.main.utils import is_server_running
from app.models import Notification


@bp.before_request
def print_headers():
    print("***** Copy Headers for Cisco Catalyst Center Webhook *****")
    print(f" Authorization: Basic {current_app.config.get('BASIC_AUTH')}")
    print(" Content-Type: application/json")
    print("***** Copy Headers for Cisco Catalyst Center Webhook *****")


# GET
@bp.get("/home")
@bp.get("/")
def index(title="Home"):
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get(
        "per_page", current_app.config.get("PER_PAGE"), type=int
    )
    notifications = db.paginate(
        sa.select(Notification).order_by(Notification.created.desc()),
        page=page,
        per_page=per_page,
        max_per_page=current_app.config.get("MAX_PER_PAGE"),
        error_out=False,
    )
    return render_template(
        "main/view.j2", notifications=notifications, title=title, page=page
    )


# GET
@bp.get("/status")
@bp.get("/server-status")
def server_status():
    status = is_server_running()
    return (
        jsonify(
            {
                "status": "up" if status else "down",
                "code": HTTPStatus.OK if status else HTTPStatus.INTERNAL_SERVER_ERROR,
            }
        ),
        (HTTPStatus.OK if status else HTTPStatus.INTERNAL_SERVER_ERROR),
        {"Content-Type": "application/json; charset=utf-8"},
    )
