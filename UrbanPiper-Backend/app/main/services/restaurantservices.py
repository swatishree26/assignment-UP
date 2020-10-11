from ..models.restaurantmodel import Category , db
from flask_sqlalchemy import sqlalchemy
from flask import current_app


def category_show():
    query = 'select * from food_categories as c;'
    food_categories = db.session.execute(query)
    ls = []
    for each in food_categories:   
        # ls.append(each.id)    
        ls.append(each.name)
    return ls

def item_desc(category):
    query = "select * from food_items as i where category_id = {} order by name asc;".format(category)
    food_items = db.session.execute(query)
    ls = []
    for each in food_items:
        row= {}
        row['id'] = each.id
        row['name'] = each.name
        row['description'] = each.description
        row['food_type'] = each.food_type
        row['price'] = each.price
        ls.append(row)
    if len(ls)==0:
        return "no products found"
    return ls


def item_search(category_id, item_name):
    query = "select * from food_items as  i where category_id = {0} and name = {1};".format(category_id, item_name)
    food_items = db.session.execute(query)
    ls = []
    for each in food_items:
        row= {}
        row['id'] = each.id
        row['name'] = each.name
        row['description'] = each.description
        row['food_type'] = each.food_type
        row['price'] = each.price
        ls.append(row)
    if len(ls)==0:
        return "no products found"
    return ls

def item_filter(filter_id):
    query = "select * from food_items as  i where food_type = {0};".format(filter_id)
    food_items = db.session.execute(query)
    ls = []
    for each in food_items:
        row= {}
        row['id'] = each.id
        row['name'] = each.name
        row['description'] = each.description
        row['food_type'] = each.food_type
        row['price'] = each.price
        ls.append(row)
    if len(ls)==0:
        return "no products found"
    return ls


