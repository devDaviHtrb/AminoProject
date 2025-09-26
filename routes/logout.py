from flask import Blueprint, make_response, redirect, render_template, request, url_for
from routes.GetPage import pages
logout = Blueprint("logout", __name__)

@logout.route("/logout")
def Logout():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        response = make_response(redirect(url_for("home.Home")))
        response.delete_cookie("name")
        return response
    return render_template("login.html")