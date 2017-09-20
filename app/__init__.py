import os
from flask import Flask
app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.urandom(24)

from app import views



app.config.from_object('config')