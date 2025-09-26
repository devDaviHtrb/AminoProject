from flask import Blueprint, render_template, request
from routes.GetPage import pages
home = Blueprint("home", __name__)

@home.route("/")
def Home():
    if request.cookies.get("name"):
        routes = ["communities", "chat", "logout"]
    else:
        routes = ["communities", "chat", "login"]
    return render_template("Home.html", routes=routes) #pages = pages.keys()) n tem pq colocar, pois as comunidades mais famosas são predefinidas, mas usei a renderização dinamica no menu da home