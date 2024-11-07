
from flask import Flask, jsonify, request
from routes.recipe_blueprint import recipe_blueprint
from routes.ingredient_blueprint import ingredient_blueprint

app = Flask(__name__)
app.register_blueprint(recipe_blueprint, url_prefix='/recipes')
app.register_blueprint(ingredient_blueprint, url_prefix='/ingredients')

@app.route('/')
def home():
    return "Welcome to the Interactive Recipe Manager!"

if __name__ == '__main__':
    app.run(debug=True)
