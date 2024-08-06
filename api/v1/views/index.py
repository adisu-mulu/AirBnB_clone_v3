#!/usr/bin/python3
"""This module defines the status route"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returning status on status"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def num_of_each_objects():
    """ retrieve number of each objects"""
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objects = {}
    for i in range(len(classes)):
        num_objects[names[i]] = storage.count(classes[i])
    return jsonify(num_objects)
