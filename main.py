from flask import Flask, redirect, url_for, render_template, request, session
import db

app = Flask(__name__)

app.secret_key = 'pes'


@app.route('/', methods=["POST", "GET"])
def home():
	if "user" in session:
		user = '<i>Signed in as ' + session['user'] + '</i>'
		username = session['user']
		icon = "glyphicon glyphicon-user"
		classs = 'hidden'

		if request.method == "POST":
			content = request.form['ct']
			db.post(username, content)

	else:
		user = 'Login'
		icon = 'glyphicon glyphicon-log-in'
		classs = ''

	return render_template('index.html', content='TacticalForum', user=user, icon=icon, classs=classs, posts=db.load_feed())


@app.route('/user')
def user():
	if "user" in session:
		user = '<i>Signed in as ' + session['user'] + '</i>'
		icon = "glyphicon glyphicon-user"
		menofka = session['user']
		classs = 'hidden'
		return render_template('logged_in.html', user=user, menofka=menofka, icon=icon, classs=classs)

	else:
		return redirect(url_for('login'))


@app.route("/admin")
def admin():
	return redirect(url_for("user", name='Admin!'))


@app.route("/login", methods=["POST", "GET"])
def login():
	user = 'Login'
	icon = 'glyphicon glyphicon-log-in'

	if request.method == "POST":
		session.permanent = True
		username = request.form["nm"]
		password = request.form['pw']

		if db.login(username, password) == True:
			session["user"] = username
			return redirect(url_for("user"))

		elif db.login(username, password) == 'wp':
			return "Wrong password"

		else:
			return "Please register"
	
	else:
		if "user" in session:
			return redirect(url_for("user"))

		return render_template("login.html", user=user, icon=icon)


@app.route("/register", methods=["POST", "GET"])
def register():
	user = 'Login'
	icon = 'glyphicon glyphicon-log-in'
	if request.method == "POST":
		session.permanent = True
		username = request.form["nm"]
		password = request.form['pw']
		if db.register(username, password):
			return redirect(url_for("user"))

		else:
			print('Already registered, please log in.')

	else:
		if "user" in session:
			return redirect(url_for("user"))

		return render_template("register.html", user=user, icon=icon)


@app.route('/logout')
def logout():
	session.pop('user', None)
	return redirect(url_for('login'))


if __name__ == "__main__":
	app.run()