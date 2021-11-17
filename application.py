
from flask import Flask, request, Response
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.errors import errors
from flask_jwt_extended import JWTManager
from flask_mail import Mail

app = Flask(__name__)
#app.config.from_envvar('ENV_FILE_LOCATION')
app.config.from_json("config")
mail = Mail(app)

@app.route("/")
def home_view():
        return "<h1>Welcome to Christian's backend task</h1>"

from resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)



initialize_db(app)
initialize_routes(api)
