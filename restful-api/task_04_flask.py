#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
	return "Welcome to the Flask API!"

users = {}

@app.route("/data")
def json_function():
	return jsonify(list(users.keys()))

@app.route("/status")
def status_function():
	return "OK"

@app.route("/users/<username>")
def dynamic_content_func(username):
	if username in users:
		return jsonify(users[username])
	else:
		return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
	data = request.get_json()
	username = data.get("username")
	if username not in data:
		return jsonify({"error": "Username is required"}), 400
	
	name = data["username"]

	users[name] = data
	message = {
		"message": f"User added",
		"user": data
	}
	return jsonify(message), 201

if __name__ == "__main__": app.run()