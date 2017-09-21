#views.py

from flask import render_template, session
from app import app
# @app.route('/')
# def index():
# 	return render_template("login.html")

# @app.route('/home')
# def home():
# 	return render_template("dashboard.html")


@app.route('/login')
def login():
	session['user'] = 'Symon'
	return render_template('login.html')

@app.route('/')
def dashboard():
	session['user'] = 'Symon'
	return render_template('dashboard.html')	

@app.route('/signup')
def signup():
	session['user'] = 'Symon'
	return render_template('signup.html')

@app.route('/getsession')
def getsession():
	if 'user' in session:
		return sesion['user']

	return 'Not logged in'
	
@app.route('/dropsession')
def dropsession():
	session.pop('user', none)
	return 'Dropped!'