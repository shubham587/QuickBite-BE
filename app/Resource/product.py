# from flask import request
# from flask_restful import Resource
# from app import db
# from bson import json_util
# import json

# class Product(Resource):
#     def get(self):
#         res = json.loads(json_util.dumps(db.get_all_food_item()))
#         return res


from flask_restful import Resource
from flask import request, jsonify, json
from app import db
from flask_jwt_extended import jwt_required
from bson import json_util
from ..Schema.ProductSchema import ProductSchema
from marshmallow import ValidationError

class Product(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        global is_list

        # validate wheather the json_data is only one or multiple
        if isinstance(data, list):
            # Validate the data
            is_list = True
            food_item_schema = ProductSchema(many=True)
        else:
            # Validate the data
            is_list = False
            food_item_schema = ProductSchema(many=False)
            
        try:
            validated_data = food_item_schema.load(data)
        except ValidationError as v_err:
            return {"errors": v_err.messages}, 403
        
        # if is_list:
        #     for item in validated_data:
        #         product = ProductModel(item)
                
        
        return {"msg": "success", "v_data": validated_data}, 200
    @jwt_required()
    def get(self):
        location = request.args.get("location")
        seller_name = request.args.get("seller_name")
        food_pref = request.args.get("type")
        
        def err_response(err_msg, err_code):
            return {"errors": err_msg}, err_code
        
        #check for location "non - global" location
        if location and location != "global":
            if seller_name:
                ret = json.loads(json_util.dumps(db.get_product_by_location_seller(location, seller_name, food_pref)))
                err_msg = f"The seller or food type is not available in {location} location"
                err_code = 404
            else:
                ret = json.loads(json_util.dumps(db.get_product_by_location(location, food_pref)))
                err_msg = "The seller not found"
                err_code = 404
        # check for global
        elif location == "global":
            # check global with specific seller
            if seller_name:
                ret = json.loads(json_util.dumps(db.get_all_seller_product(seller_name, food_pref)))
                err_msg = "The Seller not found"
                err_code = 404
            # get all available data (all seller)
            else:
                ret = json.loads(json_util.dumps(db.get_all_product(food_pref)))
                err_msg = "No Data Found!!"
                err_code = 404
        else:
            err_msg = "Please provide a valid parameter"
            err_code = 400
        
        seller = set()
            
        if ret:
            for item in ret:
                # print(item["seller_name"])
                seller.add(item["seller_name"])
                
            seller_lst = [item for item in seller]
            return {"msg": "success","seller_list":seller_lst, "data": ret}, 200
        else:
            return err_response(err_msg, err_code)
        