from flask import Blueprint, render_template, request, redirect, url_for

DragonBallWiki = Blueprint("DragonBallWiki", __name__)

@DragonBallWiki.route("/DragonBallWiki")
def dragonBallWiki():
    return  render_template("DragonBallWiki.html")