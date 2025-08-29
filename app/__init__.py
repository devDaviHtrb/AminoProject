from flask import Flask
from app.setup.registerRoutes import register_routes
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


  
    register_routes(app)

    return app