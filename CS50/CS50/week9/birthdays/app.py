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

        # TODO: Add the user's entry into the database
        # read data
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # add data to db
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?);", name, month, day)


        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        # select all birthday in table and assign result to variable
        bday=db.execute("SELECT * FROM birthdays;")

        return render_template("index.html", birthdays = bday)


@app.route("/delete", methods=["POST"])
def delete_birthday():
    # Retrieve the birthday_id from the form submission
        birthday_id = request.form.get("birthday_id")

        # delete the birthday entry with the given ID
        db.execute("DELETE FROM birthdays WHERE id =(?)", birthday_id)

        return redirect("/")
