#!/usr/bin/python3
""" This module define the teardown context """
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(error):
    """closing the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def nop(error):
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    """Starting function"""
    # Get host and port from environment variables or set default values
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))

    # Run the Flask application with specified host, port, and threading
    app.run(host=host, port=port, threaded=True, debug=True)
