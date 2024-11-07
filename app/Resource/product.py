from flask import request
from flask_restful import Resource
from app import db
from bson import json_util
import json

class Product(Resource):
    def get(self):
        res = json.loads(json_util.dumps(db.get_all_food_item()))
        return res