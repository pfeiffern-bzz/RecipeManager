
from flask import Blueprint, jsonify
from utils.algorithm_utils import unique_ingredients

ingredient_blueprint = Blueprint('ingredient_blueprint', __name__)

@ingredient_blueprint.route('/', methods=['GET'])
def get_all_ingredients():
    ingredients = unique_ingredients()
    return jsonify({"ingredients": ingredients})
