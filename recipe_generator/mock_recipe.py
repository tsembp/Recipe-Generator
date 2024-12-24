import json

def load_mock_recipes(filepath="data/example_recipes.json"):
    with open(filepath, "r") as file:
        return json.load(file)

def generate_mock_recipe(ingredients):
    recipes = load_mock_recipes()
    for recipe, required_ingredients in recipes.items():
        if all(item.strip() in ingredients for item in required_ingredients):
            return f"You can make {recipe} with your ingredients!"
    return "Sorry, no matching recipe found."
