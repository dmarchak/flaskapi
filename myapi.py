#!/usr/bin/env python3

"""A simple Flask API that returns a JSON response."""

from functools import wraps
from flask import Flask, request, jsonify, Response
from classes.car import Car


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello():
    """Endpoint to return a JSON response."""
    return jsonify({"message": "Hello, from your Flask API!"})

@app.route('/car', methods=['POST'])
def create_car():
    """Endpoint to create a new car."""
    data = request.json
    try:
        make = data.get('make')
        model = data.get('model')
        year = data.get('year')

        if not all([make, model, year]):
            return jsonify({"error": "Missing required fields"}), 400

        car = Car(make=make, model=model, year=year)
        return jsonify({"car": car.__dict__}), 201

    except (TypeError, ValueError) as e:
        return jsonify({"error": str(e)}), 500

###
# Authentication Logic
###

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'secret'

def check_auth(username, password):
    """Check if a username/password combination is valid."""
    return username == VALID_USERNAME and password == VALID_PASSWORD

def authenticate():
    """Sends a 401 response that enables basic auth."""
    return Response('Could not validate your credentials.',401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    """Decorator to prompt for authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

###
# Stop Auth Logic
###

@app.route('/protected')
@requires_auth
def protected():
    """A protected endpoint that requires authentication."""
    return jsonify({"message": "This is a protected endpoint. You are authenticated!"})


if __name__ == '__main__':
    app.run(debug=True)
