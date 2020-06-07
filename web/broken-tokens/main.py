import jwt
import base64
import os
import hashlib
from flask import Flask, render_template, make_response, request, redirect
app = Flask(__name__)
FLAG = os.getenv("FLAG")
PASSWORD = os.getenv("PASSWORD")
with open("privatekey.pem", "r") as f:
	PRIVATE_KEY = f.read()
with open("publickey.pem", "r") as f:
	PUBLIC_KEY = f.read()

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		resp = make_response(redirect("/"))
		if request.form["action"] == "Login":
			if request.form["username"] == "admin" and request.form["password"] == PASSWORD:
				auth = jwt.encode({"auth": "admin"}, PRIVATE_KEY, algorithm="RS256")
			else:
				auth = jwt.encode({"auth": "guest"}, PRIVATE_KEY, algorithm="RS256")
			resp.set_cookie("auth", auth)
		else:
			resp.delete_cookie("auth")
		
		return resp
	else:
		auth = request.cookies.get("auth")
		if auth is None:
			logged_in = False
			admin = False
		else:
			logged_in = True
			admin = jwt.decode(auth, PUBLIC_KEY)["auth"] == "admin"
		resp = make_response(
			render_template("index.html", logged_in=logged_in, admin=admin, flag=FLAG)
		)
	return resp

@app.route("/publickey.pem")
def public_key():
	with open("./publickey.pem", "r") as f:
		resp = make_response(f.read())
		resp.mimetype = 'text/plain'
		return resp

if __name__ == "__main__":
	app.run()