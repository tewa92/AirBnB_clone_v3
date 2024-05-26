#!/usr/bin/python3
"""
This module sets up the Blueprint for the API views.
"""

from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
