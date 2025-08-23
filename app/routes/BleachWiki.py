from flask import Blueprint, render_template, request, redirect, url_for

BleachWiki = Blueprint("BleachWiki", __name__)

@BleachWiki.route("/BleachWiki")
def bleachWiki():
    return  render_template("BleachWiki.html")