from flask import Blueprint, render_template, request, redirect, url_for

OnePieceWiki = Blueprint("OnePieceWiki", __name__)

@OnePieceWiki.route("/OnePieceWiki")
def onePieceWiki():
    return  render_template("OnePieceWiki.html")