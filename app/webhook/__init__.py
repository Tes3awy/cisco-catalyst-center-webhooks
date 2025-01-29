# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint("webhook", __name__, template_folder="templates")

from app.webhook import views
