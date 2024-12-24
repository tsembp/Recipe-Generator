import openai

# Set your API key
openai.api_key = "api-key-here"

def generate_ai_recipe(ingredients):
    prompt = f"Suggest a recipe using these ingredients: {', '.join(ingredients)}."
    try:
        # Use the new API structure
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=100
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error generating recipe: {str(e)}"
