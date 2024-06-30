from flask import Flask, jsonify
from flask_cors import CORS
from .model.Ability import AbilityRepository, Ability
import os

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
    ability_repo = AbilityRepository()
    ability_repo.read_tsv("ref/Pokemon-Abilities.tsv")
    ability_repo.dump_records()
    app.config['ABILITIES'] = ability_repo.jsonify_abilities()

    from .routes import main
    app.register_blueprint(main)

    return app


