# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint("main", __name__, template_folder="templates")

from app.main import views
