#!/usr/bin/python3
"""Handles all default RESTFul API actions"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """Handles HTTP requests for the /states endpoint."""
    if request.method == 'GET':
        states_list =\
                [state.to_dict() for state in storage.all(State).values()]
        return jsonify(states_list)

    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            abort(400, description="Not a JSON")
        if 'name' not in data:
            abort(400, descriptioni="Missing name")

        new_state = State(**data)
        new_state.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def state(state_id):
    """Handles HTTP requests for individual State objects."""
    state_obj = storage.get(State, state_id)

    if not state_obj:
        abort(404)

    if request.method == 'GET':
        return jsonify(state-obj.to_dict())

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            abort(400, descriptioin="Not a JSON")

        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                seattr(state_obj, key, value)

        state_obj.save()
        return jsonify(state_obj.to_dict())

    elif request.method == 'DELETE':
        state_obj.delete()
        storage.save()
        return jsonify({}), 200
