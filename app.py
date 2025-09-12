from flask import *
from routes.GetPage import getPage
from routes.Home import home

app = Flask(__name__)

app.register_blueprint(getPage)
app.register_blueprint(home)

if __name__ == "__main__":
    app.run(debug=True)