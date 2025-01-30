# -*- coding: utf-8 -*-
from http import HTTPStatus

from flask import jsonify, request, url_for

from app import basic_auth, db, socketio
from app.models import Notification
from app.webhook import bp


# POST
@bp.post("/webhook")
@basic_auth.required
def webhook():
    print("Webhook Received")
    notificaion = Notification(
        event_id=request.json.get("eventId"),
        namespace=request.json.get("namespace"),
        name=request.json.get("name"),
        descr=request.json.get("description"),
        event_type=request.json.get("type"),
        category=request.json.get("category"),
        domain=request.json.get("domain"),
        subdomain=request.json.get("subDomain"),
        severity=request.json.get("severity"),
        source=request.json.get("source"),
        timestamp=request.json.get("timestamp"),
        details_type=request.json.get("details").get("Type"),
        priority=request.json.get("details").get("Assurance Issue Priority"),
        issue=request.json.get("details").get("Assurance Issue Details"),
        device=request.json.get("details").get("Device"),
        issue_name=request.json.get("details").get("Assurance Issue Name"),
        issue_category=request.json.get("details").get("Assurance Issue Category"),
        status=request.json.get("details").get("Assurance Issue Status"),
        link=request.json.get("ciscoDnaEventLink"),
    )
    db.session.add(notificaion)
    db.session.commit()

    socketio.emit(
        "event", {"data": notificaion.serialize}, namespace=url_for("main.index")
    )

    # You can add the logic of sending an email here as well
    # Check https://realpython.com/python-send-email/

    return (
        jsonify(
            {
                "msg": "Webhook notification received and saved to the DB",
                "code": HTTPStatus.CREATED,
            }
        ),
        HTTPStatus.CREATED,
    )
