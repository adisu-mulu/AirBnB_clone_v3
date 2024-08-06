#!/usr/bin/python3
"""this module defines states """
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, make_response, request


@app_views.route('/states', strict_slashes=False)
def get_all_states():
    """retrieves all states"""
    states = storage.all(State).values()
    list_s = []

    for sts in states:
        list_s.append(sts.to_dict())

    return jsonify(list_s)


@app_views.route('/states/<state_id>', strict_slashes=False)
def state_state_id(state_id):
    """ retrieve using state_id"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state_id(state_id):
    """deletes a state"""
    states = storage.get(State, state_id)
    if not states:
        abort(404)
    storage.delete(states)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """create new state"""

    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    instance = State(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def state_put(state_id):
    """update state"""
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()), 200)
