from flask import Flask, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='static/build')
    CORS(app)

    # Read key-value pairs from a file or define them here
    data = [
        {"key": "key1", "value": "value1"},
        {"key": "key2", "value": "value2"},
        {"key": "key3", "value": "value3"}
    ]
    app.config['DATA'] = data

    from .routes import main
    app.register_blueprint(main)

    return app


