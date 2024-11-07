
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

def check_user(email):
    return db_init.User.find_one({"email": email})

def reqister_user(username, email, password):
    return db_init.User.insert_one({"username": username, "email": email, "password": password})

def add_to_blacklist(jti):
    return db_init.BlackList.insert_one({"jti": jti})

def check_token_blacklist(jti):
    return db_init.BlackList.find_one({"jti": jti})