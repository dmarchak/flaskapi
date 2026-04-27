#!/usr/bin/env python3

"""A simple Flask API that returns a JSON response."""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello():
    """Endpoint to return a JSON response."""
    return jsonify({"message": "Hello, from your Flask API!"})

if __name__ == '__main__':
    app.run(debug=True)
