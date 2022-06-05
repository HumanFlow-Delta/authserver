#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
from models import *

@app.route("/auth/<username>/<password>")
def authenticate(id, password):
    User.query.filter_by
