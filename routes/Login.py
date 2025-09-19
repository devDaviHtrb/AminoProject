from flask import Blueprint, render_template
from routes.GetPage import pages
login = Blueprint("login", __name__)

@login.route("/Login")
def Login():
    return render_template("login.html")