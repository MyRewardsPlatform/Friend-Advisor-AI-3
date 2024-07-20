# api.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, Unauthorized
from auth import User, authenticate, identity
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from database import Database
from blockchain import Blockchain
from score_update import ScoreUpdate
from config import API_CONFIG

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = API_CONFIG['API_SECRET']
jwt = JWTManager(app)

db_instance = Database()
blockchain_instance = Blockchain()
score_update_instance = ScoreUpdate()

@app.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        raise BadRequest("Missing JSON in request")

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        raise BadRequest("Missing username parameter")
    if not password:
        raise BadRequest("Missing password parameter")

    user = User(username, password)
    user.save_to_db()

    return jsonify({"msg": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        raise BadRequest("Missing JSON in request")

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        raise BadRequest("Missing username parameter")
    if not password:
        raise BadRequest("Missing password parameter")

    user = User.find_by_username(username)
    if user and user.check_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        raise Unauthorized("Bad username or password")

@app.route('/score', methods=['GET'])
@jwt_required
def get_score():
    current_user = get_jwt_identity()
    user = User.find_by_username(current_user)
    if user:
        score = score_update_instance.get_score(user.id)
        return jsonify(score=score), 200
    else:
        raise BadRequest("User not found")

if __name__ == '__main__':
    app.run(debug=True)
