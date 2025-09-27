from flask import *
from flask_socketio import SocketIO, join_room, rooms
from routes.logout import logout
from routes.chat import chat
from routes.GetPage import getPage
from routes.Home import home
from routes.Login import login
from routes.chat import chatsList

app = Flask(__name__)
socket = SocketIO(app)

@socket.on("joinRoom")
def join(infos):
    animeName = infos
    join_room(animeName)
  

@socket.on("message")
def msg(data):
    origin = request.sid
    roomsChat = [room for room in rooms() if room != origin]
    room = roomsChat[0]
    msgTxt = data["msg"]
    socket.emit("message", {"msg":msgTxt, "id":origin, "name": request.cookies.get("name")}, room=room)
    chatsList[room].append({"user":request.cookies.get("name"), "msg":data["msg"]})

app.register_blueprint(getPage)
app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(chat)
app.register_blueprint(logout)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("404Error.html"), 404

@app.errorhandler(401)
def pageNotFound(error):
    return redirect(url_for("login.Login")), 404

if __name__ == "__main__":
    socket.run(app=app, debug=True)