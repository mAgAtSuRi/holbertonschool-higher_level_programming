#!/usr/bin/python3
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()
app = Flask(__name__)
users = {
	"John": generate_password_hash("hello"),
	"Susan": generate_password_hash("bye")
}


@auth.verify_password
def verify_password(username, password):
	if username in users and \
            check_password_hash(users.get(username), password):
		return username
print(users)


@app.route('/')
@auth.login_required
def index():
	return f"Hello, {auth.current_user()}"

if __name__ == '__main__':
    app.run()