import sqlalchemy as sa
from flask import current_app, jsonify, render_template

from app import basic_auth, db
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
@bp.get("/")
@basic_auth.required
def list():
    notifications = db.session.scalars(
        sa.select(Notification).order_by(Notification.created.desc())
    )
    return render_template("main/view.j2", notifications=notifications)


# GET
@bp.get("/server-status")
def server_status():
    status = is_server_running()
    return jsonify({"status": "up" if status else "down"}), 200 if status else 500
