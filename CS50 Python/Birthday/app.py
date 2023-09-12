import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        error = ""
        field_name = request.form.get("field_name")
        field_day = request.form.get("field_day")
        field_month = request.form.get("field_month")
        if not field_name:
            error = "No name provided!"
        elif not field_day:
            error = "No date provided!"
        elif not field_month:
            error = "No month provided!"
        else:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES(?,?,?)", field_name, field_month, field_day)
            bday = db.execute("SELECT * FROM birthdays")
            return render_template("index.html", message=error, birthdays=bday)
    else:
        bday = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=bday)
