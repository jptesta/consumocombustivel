from flask import render_template, request, redirect, url_for, flash

from app import app
from app import db

@app.route("/")
def index():
    return render_template("index.html")
