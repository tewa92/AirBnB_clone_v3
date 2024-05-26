from flask import Blueprint, jsonify, abort, request
from models import storage
from models.state import State

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(states), 200

@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict()), 200

@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State"""
    if not request.is_json:
        abort(400, description="Not a JSON")
    body = request.get_json()
    if 'name' not in body:
        abort(400, description="Missing name")
    new_state = State(**body)
    new_state.save()
    return jsonify(new_state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State object"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    body = request.get_json()
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in body.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
