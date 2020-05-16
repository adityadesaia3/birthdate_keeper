from flask import Flask, render_template, request, flash, redirect, url_for
import os
from birthdate_db import add_birthdate_to_db, create_db

app = Flask(__name__)

# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
app.secret_key = b"K5VN^;WLzmtxj[P7"

# Path of current directory
current_directory_path = os.path.dirname(os.path.realpath(__file__))


@app.route("/")
def index():
    create_db()
    return render_template("index.html")

@app.route("/add_birthdate")
def add_birthdate():
    return render_template("add_birthdate.html")

@app.route("/add_birthdate_db", methods=["GET", "POST"])
def add_birthdate_db():
    name = request.form["name"]
    birthdate = request.form["birthdate"]

    add_birthdate_to_db(name, birthdate)

    return render_template("add_birthdate.html")

@app.route("/display_birthdates")
def display_birthdates():
    return render_template("display_birthdates.html")

if __name__ == "__main__":
    app.run(debug=True)