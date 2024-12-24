def validate_ingredients(ingredients):
    if not ingredients:
        raise ValueError("No ingredients provided.")
    return [item.strip() for item in ingredients]
