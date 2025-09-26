from flask import abort, render_template, Blueprint, request

chatsList = {"naruto":[], "dragon ball":[], "bleach":[], "one piece":[]}
chat = Blueprint("chat", __name__)
@chat.route("/chat/<anime>")
def Chat(anime):
    if anime not in chatsList:
        abort(404)
    return render_template("chat.html", anime=anime, chat=chatsList[anime], user=request.cookies.get("name"))