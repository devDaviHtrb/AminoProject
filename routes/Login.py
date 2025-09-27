from flask import Blueprint, make_response, redirect, render_template, request, url_for
from routes.GetPage import pages
login = Blueprint("login", __name__)


names = []
@login.route("/login", methods=["POST", "GET"])
@login.route("/login/<msg>", methods=["POST", "GET"])
def Login(msg=""):
    msg = msg
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        if name in names:
            return redirect(url_for("login.Login", msg = "This name already have been used"))
        
        response = make_response(redirect(url_for("home.Home")))
        response.set_cookie("name", name)
        
        names.append(name)
        return response
    return render_template("login.html", msg=msg)