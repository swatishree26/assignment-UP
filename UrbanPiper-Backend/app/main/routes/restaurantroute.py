from flask import Blueprint
from flask import request
import datetime
from flask import jsonify
from ..services.restaurantservices import *
import json


restaurant = Blueprint("restaurant" , __name__)

@restaurant.route("/show", methods = ["GET"])
def show():
    resp = category_show()
    return jsonify({"food_categories": resp})

@restaurant.route("/show/<category_id>", methods = ['GET'])
def show_item(category_id):
    resp = item_desc(category_id)
    return jsonify({"food_items": resp})


@restaurant.route("/search/<category_id>", methods= ['GET'])
def search_item(category_id):
    name = request.args.get('name')
    resp = item_search(category_id, name)
    return json.dumps({"msg": resp})
   
@restaurant.route("/filter", methods= ['GET'])
def filter_foodtype():
    food_type = request.args.get('food_type')
    resp = item_filter(food_type)
    return json.dumps({"msg": resp})
   

