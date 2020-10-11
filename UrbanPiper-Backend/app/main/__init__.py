
from flask import Flask, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from ..config import app_config
from app.main.routes.restaurantroute import restaurant


def create_app(environ):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[environ])
    # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Welcome@123@localhost/fooddetails"
    app.config.from_pyfile("config.py")
    db.init_app(app)
    app.register_blueprint(restaurant, url_prefix='')

    return app
