from flask import Blueprint, render_template, request, redirect, url_for

NarutoWiki = Blueprint("NarutoWiki", __name__)

@NarutoWiki.route("/")
def narutoWiki():
    if request.method == "POST":
        render_template("NarutoWiki.html")
    else:
        return redirect(url_for("NarutoWiki"))