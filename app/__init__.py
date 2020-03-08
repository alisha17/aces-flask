from flask import Flask
from flask_cors import CORS
import mongoengine
from flask_jwt_extended import JWTManager


app = Flask(__name__)

app.config.from_object("config")

CORS(app, support_credentials=True)

jwt = JWTManager(app)

mongo_connection = mongoengine.connect(
    app.config["DATABASE_NAME"],
    host=app.config["DATABASE_HOST"],
    port=app.config["DATABASE_PORT"],
)

try:
    info = mongo_connection.server_info()  # Forces a call.
except Exception:
    raise Exception("mongo server is down.")

from app.controller import *
