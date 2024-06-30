from flask import Blueprint, current_app, send_from_directory, jsonify
import json

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return send_from_directory('static/build', 'index.html')

@main.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('static/build', path)

@main.route('/list')
def get_list():
    data = current_app.config['DATA']
    return jsonify(data)

@main.route('/abilities')
def get_ability_list():
    return current_app.config['ABILITIES']

