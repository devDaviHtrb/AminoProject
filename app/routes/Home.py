from flask import Blueprint, render_template, request, redirect, url_for

home = Blueprint("home", __name__)

@home.route("/")
def Home():
   return render_template("Home.html", routes=["communities", "chat", "Login"])
   