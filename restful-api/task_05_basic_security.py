#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, JWTManager
from flask_jwt_extended import jwt_required, get_jwt_identity

from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret_key"

jwt = JWTManager(app)

users = {
    "user1": {
		"username": "user1",
		"password": generate_password_hash("password"),
		"role": "user"
		},
    "admin1": {
		"username": "admin1",
		"password": generate_password_hash("password"),
		"role": "admin"
		}
}


@auth.verify_password
def verify_password(username, password):
	if username in users and check_password_hash(users[username]['password'], password):
	    return username



@app.route('/basic-protected')
@auth.login_required
def index():
	return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username not in users or not check_password_hash(users[username]['password'], password):
        return jsonify({'msg': '401 Unauthorized'}), 401	
    token = create_access_token(identity=username)
    return jsonify(access_token=token), 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
     return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def check_admin():
     current_user = get_jwt_identity()
     if users[current_user]['role'] != 'admin':
          return jsonify({"error": "Admin access required"}), 403
     return "Admin Access: Granted"

if __name__ == '__main__':
    app.run()