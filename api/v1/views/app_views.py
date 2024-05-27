#!/usr/bin/python3
"""
This module sets up the API views for the application using Flask and
Blueprint.

It includes the creation of a Blueprint instance for the API views and defines
the routes  for the application, specifically the '/status' endpoint.
"""

from flask import Blueprint, jsonify

# Create a Blueprint instance for the API views with the URL prefix '/api/v1'
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route('/status', methods=['GET'])
def status():
    """
    Define the '/status' route that returns a JSON response indicating the
    status of the API.

    Returns:
        Response: A Flask JSON response with a status key set to "OK".
    """
    return jsonify({"status": "OK"})
