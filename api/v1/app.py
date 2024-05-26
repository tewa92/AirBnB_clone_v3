#!/usr/bin/python3
"""
Flask application setup
"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

# Enable CORS for all routes and allow requests from any origin
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Register the blueprint for API routes
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """
    Closes the storage on teardown
    """
    storage.close()


@app.errorhandler(404)
def not_found_error(exception):
    """
    Handle 404 errors with a custom JSON response
    :return: JSON response with error message and 404 status code
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    # Run the Flask application with host and port from environment variables
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"), port=int(getenv("HBNB_API_PORT", 5000)))
