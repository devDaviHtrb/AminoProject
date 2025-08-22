from flask import Flask
from flask_socketio import SocketIO
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    socketIo = SocketIO(app)

    from app.routes.Home import home
    app.register_blueprint(home)

    from app.routes.NarutoWiki import NarutoWiki
    app.register_blueprint(NarutoWiki)

    from app import sockets

    return {"app":app, "socket":socketIo}