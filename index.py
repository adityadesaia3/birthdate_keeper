from flask import Flask, render_template, request, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
from birthdate_db import add_birthdate_to_db, create_db, get_max_id, fetch_birthdates_from_db, fetch_single_birthdate_from_db, update_birthdate_from_db, delete_birthdate_from_db, fetch_birthdates_today

app = Flask(__name__)

# https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
app.secret_key = b"K5VN^;WLzmtxj[P7"

# Path of current directory
current_directory_path = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = current_directory_path + "/static/uploaded_photos/"
os.makedirs("static/uploaded_photos", exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    create_db()
    birthdates_today = fetch_birthdates_today()
    return render_template("index.html", birthdates_today = birthdates_today)

@app.route("/add_birthdate_db", methods=["GET", "POST"])
def add_birthdate_db():
    name = request.form["name"]
    birthdate = request.form["birthdate"]
    photo = request.files["photo"]
    photo_name = None
    if photo: photo_name = secure_filename(photo.filename)
    try:
        if allowed_file(photo_name):
            # get maximum unique id from the database
            photo_name = f"{str(get_max_id() + 1)}.{photo_name.rsplit('.')[1].lower()}"
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_name))
    except:
        photo_name = None

    # Add input birthdate data to database
    add_birthdate_to_db(name, birthdate, photo_name)

    return redirect(url_for("index"))

@app.route("/display_birthdates")
def display_birthdates():
    birthdate_data = fetch_birthdates_from_db()
    return render_template("display_birthdates.html", birthdate_data = birthdate_data)


@app.route("/update_birthdate", methods=("GET", "POST"))
def update_birthdate():
    b_id = request.form["b_id"]
    birthdate_data = fetch_single_birthdate_from_db(b_id)
    return render_template("update_birthdate.html", birthdate_data=birthdate_data)


@app.route("/delete_birthdate", methods=("GET", "POST"))
def delete_birthdate():
    b_id = request.form["b_id"]
    birthdate_data = fetch_single_birthdate_from_db(b_id)
    return render_template("delete_birthdate.html",  birthdate_data=birthdate_data)


@app.route("/update_birthdate_db", methods=("GET", "POST"))
def update_birthdate_db():
    b_id = request.form["b_id"]
    name = request.form["name"]
    birthdate = request.form["birthdate"]
    photo = request.files["photo"]

    photo_name = None
    if photo: photo_name = secure_filename(photo.filename)
    try:
        if allowed_file(photo_name):
            # get maximum unique id from the database
            photo_name = f"{str(b_id)}.{photo_name.rsplit('.')[1].lower()}"

            # remove previous files
            dir_path = current_directory_path + "/static/uploaded_photos/"
            files_to_remove = os.listdir(dir_path)
            for file in files_to_remove:
                if file.startswith(str(b_id)):
                    os.remove(os.path.join(dir_path, file))

            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_name))
    except:
        photo_name = None

    # Add input birthdate data to database
    update_birthdate_from_db(b_id, name, birthdate, photo_name)

    return redirect(url_for("display_birthdates"))


@app.route("/delete_birthdate_db", methods=("GET", "POST"))
def delete_birthdate_db():
    b_id = request.form["b_id"]

    delete_birthdate_from_db(b_id)

    # remove all files corresponding to deleted birthdate
    dir_path = current_directory_path + "/static/uploaded_photos/"
    files_to_remove = os.listdir(dir_path)

    for file in files_to_remove:
        if file.startswith(str(b_id)):
            os.remove(os.path.join(dir_path, file))

    return redirect(url_for("display_birthdates"))


if __name__ == "__main__":
    app.run(debug=True)