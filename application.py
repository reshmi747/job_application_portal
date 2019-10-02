from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify
from flask_session import Session

from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from datetime import datetime
from cs50 import SQL
from flask_jsglue import JSGlue


# app configuration
app = Flask(__name__)
JSGlue(app)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.route("/")
def index():
    """ Display login forms for admin/users. """

    return render_template("index.html")
