#views.py

from flask import render_template

from app import app

@app.route('/')
def index():
	return render_template("login.html")

@app.route('/home')
def home():
	return render_template("dashboard.html")