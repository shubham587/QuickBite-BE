
from app import db_init

def get_all_food_item():
    return db_init.Product_Data.find({})