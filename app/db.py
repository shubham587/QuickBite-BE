
from app import db_init

def get_all_food_item(food_pref):
    if food_pref:
        return db_init.Product_Data.find({"type": food_pref})
    else:
        return db_init.Product_Data.find({})

def post_product(data):
    return db_init.Product_Data.insert_one(data)

def get_all_product(food_pref):
    if food_pref:
        return db_init.Product_Data.find({"type": food_pref})
    else:
        return db_init.Product_Data.find({})


def get_product_by_location(location, food_pref):
    if food_pref:
        return db_init.Product_Data.find({"location": location, "type": food_pref})
    else:
        return db_init.Product_Data.find({"location": location})

def get_product_by_location_seller(location, seller_name, food_pref):
    if food_pref:
        return db_init.Product_Data.find({"location": location, "seller_name": seller_name, "type": food_pref})
    else:
        return db_init.Product_Data.find({"location": location, "seller_name": seller_name})


def get_all_seller_product(seller_name, food_pref):
    if food_pref:
        return db_init.Product_Data.find({"seller_name": seller_name, "type": food_pref})
    else:
        return db_init.Product_Data.find({"seller_name": seller_name})
