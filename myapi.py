#!/usr/bin/env python3

"""A simple Flask API that returns a JSON response."""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_data():
    """Endpoint to return a JSON response."""
    return jsonify({"message": "Hello, World!"})


if __name__ == '__main__':
    app.run(debug=True)
