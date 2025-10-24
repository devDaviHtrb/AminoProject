from flask import Blueprint, make_response, redirect, render_template, request, url_for
from routes.GetPage import pages
from routes.Login import names
logout = Blueprint("logout", __name__)

@logout.route("/logout")
def Logout():
   
    response = make_response(redirect(url_for("home.Home")))
    names.remove(request.cookies.get("name"))
    response.delete_cookie("name")
    return response
