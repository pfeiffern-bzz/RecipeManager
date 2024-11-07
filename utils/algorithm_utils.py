
from functools import reduce

def filter_recipes(recipes, min_prep_time=None, max_prep_time=None):
    return list(filter(lambda r: (min_prep_time is None or r.prep_time >= min_prep_time) and
                                  (max_prep_time is None or r.prep_time <= max_prep_time), recipes))

def sort_recipes(recipes):
    return sorted(recipes, key=lambda r: r.prep_time)

def aggregate_ingredients(recipes):
    all_ingredients = reduce(lambda acc, r: acc + r.ingredients, recipes, [])
    ingredient_totals = {}
    for name, quantity in all_ingredients:
        if name in ingredient_totals:
            ingredient_totals[name] += quantity
        else:
            ingredient_totals[name] = quantity
    return ingredient_totals

def unique_ingredients():
    def get_ingredients(recipes):
        ingredients = {ingredient for recipe in recipes for ingredient, _ in recipe.ingredients}
        return list(ingredients)
    return get_ingredients
