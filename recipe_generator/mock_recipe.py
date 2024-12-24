import json

def load_mock_recipes(filepath="data/example_recipes.json"):
    with open(filepath, "r") as file:
        return json.load(file)

# Example of a list of mock recipes
mock_recipes = {
    "bread": "Toast with Butter",
    "tomato": "Tomato Salad",
    "lettuce": "Lettuce Wraps",
    "cucumber": "Cucumber Salad",
    "butter": "Garlic Butter Toast",
    "cheese": "Cheese Sandwich",
    "salami": "Salami Sandwich"
}

def generate_mock_recipe(ingredients):
    # Combine all ingredients into a single string
    ingredients_set = set(map(lambda x: x.strip().lower(), ingredients))
    
    # Check if any of the ingredients match the mock recipes
    matched_recipes = [mock_recipes[ingredient] for ingredient in ingredients_set if ingredient in mock_recipes]
    
    # If no match found, return a fallback recipe
    if not matched_recipes:
        return "No recipe found for these ingredients. Try again with different ones."
    
    # Join all matched recipes into one output
    recipe_output = "Mock Recipe(s) using your ingredients:\n\n" + "\n".join(matched_recipes)
    return recipe_output

