from flask import Blueprint, render_template, request, redirect, url_for

NarutoWiki = Blueprint("NarutoWiki", __name__)

@NarutoWiki.route("/NarutoWiki")
def narutoWiki():
    return  render_template("NarutoWiki.html")