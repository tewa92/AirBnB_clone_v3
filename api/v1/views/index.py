#!/usr/bin/python3
"""
This module defines the index view for the API.
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """
    Returns the status of the API.
    """
    return jsonify({"status": "OK"})
