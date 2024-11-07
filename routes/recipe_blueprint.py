
from flask import Blueprint, jsonify, request
from models.recipe import Recipe
from utils.algorithm_utils import filter_recipes, sort_recipes, aggregate_ingredients

recipe_blueprint = Blueprint('recipe_blueprint', __name__)

recipes = [
    Recipe("Pancakes", [("Flour", 200), ("Milk", 100), ("Egg", 2)], 15, "Easy"),
    Recipe("Salad", [("Lettuce", 50), ("Tomato", 30), ("Cucumber", 20)], 10, "Easy"),
    Recipe("Spaghetti", [("Pasta", 200), ("Tomato Sauce", 100)], 25, "Medium")
]

@recipe_blueprint.route('/', methods=['GET'])
def get_recipes():
    sorted_recipes = sort_recipes(recipes)
    return jsonify([recipe.__dict__ for recipe in sorted_recipes])

@recipe_blueprint.route('/add', methods=['POST'])
def add_recipe():
    data = request.json
    recipe = Recipe(data['name'], data['ingredients'], data['prep_time'], data['difficulty'])
    recipes.append(recipe)
    return jsonify({'message': 'Recipe added successfully!'}), 201

@recipe_blueprint.route('/ingredients', methods=['GET'])
def get_ingredients():
    all_ingredients = aggregate_ingredients(recipes)
    return jsonify(all_ingredients)

@recipe_blueprint.route('/filter', methods=['GET'])
def filter_recipe_by_time():
    min_time = int(request.args.get('min_time', 0))
    max_time = int(request.args.get('max_time', 30))
    filtered_recipes = filter_recipes(recipes, min_time, max_time)
    return jsonify([recipe.__dict__ for recipe in filtered_recipes])
