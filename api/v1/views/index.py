#!/usr/bin/python3
"""Defines the basic route that handles the '/status' endpiont"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """Return the status of the API"""
    return jsonify({"status": "OK"})
