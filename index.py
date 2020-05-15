from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)

# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
app.secret_key = b"K5VN^;WLzmtxj[P7"

# Path of current directory
current_directory_path = os.path.dirname(os.path.realpath(__file__))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_birthdate")
def add_birthdate():
    return render_template("add_birthdate.html")

@app.route("/display_birthdates")
def display_birthdates():
    return render_template("display_birthdates.html")

if __name__ == "__main__":
    app.run(debug=True)