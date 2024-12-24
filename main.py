from recipe_generator.mock_recipe import generate_mock_recipe
from recipe_generator.ai_recipe import generate_ai_recipe

def main():
    print("Welcome to the Recipe Generator!")
    mode = input("Choose mode (mock/ai): ").strip().lower()

    ingredients = input("Enter ingredients you have, separated by commas: ").split(',')

    if mode == "mock":
        recipe = generate_mock_recipe(ingredients)
    elif mode == "ai":
        recipe = generate_ai_recipe(ingredients)
    else:
        print("Invalid mode selected.")
        return

    print("\nGenerated Recipe:\n")
    print(recipe)

if __name__ == "__main__":
    main()
