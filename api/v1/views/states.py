# api/v1/views/states.py

"""
Routes for handling State objects and operations.
"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_all_states():
    """
    Retrieves all State objects.
    """
    state_list = [state.to_dict() for state in storage.all("State").values()]
    return jsonify(state_list)


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """
    Creates a new State object.
    """
    state_json = request.get_json(silent=True)
    if not state_json:
        abort(400, 'Not a JSON')
    if "name" not in state_json:
        abort(400, 'Missing name')

    new_state = State(**state_json)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state_by_id(state_id):
    """
    Retrieves a specific State object by ID.
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """
    Updates a specific State object by ID.
    """
    state_json = request.get_json(silent=True)
    if not state_json:
        abort(400, 'Not a JSON')

    state = storage.get("State", state_id)
    if not state:
        abort(404)

    for key, value in state_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)

    state.save()
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """
    Deletes a State object by ID.
    """
    state = storage.get("State", state_id)
    if not state:
        abort(404)

    storage.delete(state)
    storage.save()
    return jsonify({}), 200
