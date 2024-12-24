# 👨‍🍳 Recipe Generator

A Python-based Recipe Generator that suggests recipes based on the ingredients you have. The project uses OpenAI's GPT model for AI-based recipe generation and a mock recipe generator for a simpler approach.

## 🛠️ Features
- Generate recipes using AI with OpenAI's GPT model.
- Mock recipe generator for a simpler, predefined recipe suggestion.
- Interactive command-line interface (CLI) for users to input ingredients.

## 📩 Installation

### Prerequisites
- Python 3.7 or higher
- Install required Python packages using pip.

### Steps to Install:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Recipe-Generator.git
   cd Recipe-Generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Requirements
- `openai` library (for AI-based recipe generation)
- `torch` library (installed if necessary)
  
You can install the requirements with the following command:
```bash
pip install openai torch
```

### API Key
If you're using the AI mode, you'll need to set up your OpenAI API key:
1. Create an account on [OpenAI](https://platform.openai.com/signup).
2. Create a new API key from the OpenAI dashboard.
3. Set the key in the `ai_recipe.py` file:
   ```python
   openai.api_key = "api-key-here"
   ```

## How to Use
1. Run the script:
   ```bash
   python main.py
   ```

2. Choose the mode (mock/ai).
3. Enter the ingredients you have, separated by commas (e.g., bread, cheese, tomato).

### Modes:
- **mock**: Generates a simple predefined recipe based on the ingredients.
- **ai**: Uses OpenAI's GPT model to generate a more creative recipe.

<!-- ## Example Output

```bash
Welcome to the Recipe Generator!
Choose mode (mock/ai): ai
Enter ingredients you have, separated by commas: bread, cheese, garlic, lettuce

Generated Recipe:

Makes 8 servings.

Ingredients:
- 2 cups chopped fresh spinach
- 1 tsp cumin
- 1 tsp curry powder
...
``` -->

<!-- ## License
This project is open-source and available under the MIT License. -->

## Contributing
Feel free to fork this repository, submit issues, and make pull requests. Contributions are welcome!

## Acknowledgements
- OpenAI for providing the GPT models to generate creative recipes.
