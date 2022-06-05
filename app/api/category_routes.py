from flask import Blueprint, jsonify
from app.models import db, Category

category_routes = Blueprint('categories', __name__)

@category_routes.route("/")
def read_all_categories():
    categories = Category.query.all()
    return {'categories': [category.to_dict() for category in categories]}
