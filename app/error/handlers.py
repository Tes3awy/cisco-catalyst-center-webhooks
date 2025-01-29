# -*- coding: utf-8 -*-
from flask import jsonify, render_template, request
from werkzeug.exceptions import (
    HTTPException,
    InternalServerError,
    MethodNotAllowed,
    NotFound,
    BadRequest,
    Forbidden,
    NotAcceptable,
    ServiceUnavailable,
)

from app.error import bp


@bp.app_errorhandler(BadRequest)  # 400
@bp.app_errorhandler(Forbidden)  # 403
@bp.app_errorhandler(NotFound)  # 404
@bp.app_errorhandler(MethodNotAllowed)  # 405
@bp.app_errorhandler(NotAcceptable)  # 406
@bp.app_errorhandler(InternalServerError)  # 500
@bp.app_errorhandler(ServiceUnavailable)  # 503
@bp.app_errorhandler(HTTPException)
def http_request_error(e):
    if request.path.startswith("/api/"):
        return (
            jsonify(
                {
                    "code": e.code,
                    "name": e.name,
                    "error": e.description,
                }
            ),
            e.code,
        )
    else:
        return render_template("error/error.j2", e=e), e.code
