import openai

# Set API key
openai.api_key = "api-key-here"

def generate_ai_recipe(ingredients):
    # Prompt to AI model
    prompt = f"Suggest a recipe using these ingredients: {', '.join(ingredients)}."
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=100
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error generating recipe: {str(e)}"
