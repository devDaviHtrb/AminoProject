from flask import Blueprint, render_template
from routes.GetPage import pages
home = Blueprint("home", __name__)

@home.route("/")
def Home():

    return render_template("Home.html", routes=["communities", "chat", "Login"]) #pages = pages.keys()) n tem pq colocar, pois as comunidades mais famosas são predefinidas, mas usei a renderização dinamica no menu da home