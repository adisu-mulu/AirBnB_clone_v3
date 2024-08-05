#!/usr/bin/python3
"""This module defines the status route"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """returning status on status"""
    return jsonify({"status": "OK"})
