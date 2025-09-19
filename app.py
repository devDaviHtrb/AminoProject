from flask import *
from routes.GetPage import getPage
from routes.Home import home
from routes.Login import login

app = Flask(__name__)

app.register_blueprint(getPage)
app.register_blueprint(home)
app.register_blueprint(login)

if __name__ == "__main__":
    app.run(debug=True)