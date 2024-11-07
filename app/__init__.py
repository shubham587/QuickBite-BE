from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_pymongo import MongoClient
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os
from datetime import timedelta

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app)

#DB
client = MongoClient(os.getenv("MONGO_URI"))
db_init = client.QuickBite

jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(weeks=1)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

# Token blocklist checker
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    token = db_init.BlackList.find_one({"jti": jti})
    return token is not None

from app.Resource.product import Product

api.add_resource(Product, "/product")
