import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from recipe_generator.mock_recipe import generate_mock_recipe
from recipe_generator.ai_recipe import generate_ai_recipe

# Function to generate recipe based on user input
def generate_recipe():
    ingredients = entry_ingredients.get().split(',')
    mode = selected_mode.get()

    if mode == "mock":
        recipe = generate_mock_recipe(ingredients)
    elif mode == "ai":
        recipe = generate_ai_recipe(ingredients)
    else:
        messagebox.showerror("Invalid Mode", "Please select either 'mock' or 'ai'.")
        return

    # Display the generated recipe
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, recipe)

# Create the main window
root = tk.Tk()
root.title("Recipe Generator")
root.geometry("600x500")
root.config(bg="#f7f7f7")

# Custom font settings
font_heading = ("Helvetica", 16, "bold")
font_label = ("Helvetica", 12)
font_button = ("Helvetica", 12, "bold")

# Add a label for the title
label_title = tk.Label(root, text="Welcome to the Recipe Generator!", font=font_heading, bg="#f7f7f7", fg="#4CAF50")
label_title.pack(pady=20)

# Add a label for the mode selection
label_mode = tk.Label(root, text="Choose Mode (mock/ai):", font=font_label, bg="#f7f7f7")
label_mode.pack(pady=10)

# Add a radio button for mode selection
selected_mode = tk.StringVar(value="mock")
radio_mock = ttk.Radiobutton(root, text="Mock", variable=selected_mode, value="mock")
radio_mock.pack(pady=5)
radio_ai = ttk.Radiobutton(root, text="AI", variable=selected_mode, value="ai")
radio_ai.pack(pady=5)

# Add an entry box for ingredients input
label_ingredients = tk.Label(root, text="Enter ingredients (comma-separated):", font=font_label, bg="#f7f7f7")
label_ingredients.pack(pady=10)

entry_ingredients = ttk.Entry(root, font=font_label, width=40)
entry_ingredients.pack(pady=5)

# Add a button to generate the recipe
generate_button = ttk.Button(root, text="Generate Recipe", command=generate_recipe, style="TButton")
generate_button.pack(pady=20)

# Add a text box to display the generated recipe
output_text = tk.Text(root, font=("Helvetica", 12), width=60, height=10, wrap=tk.WORD, bd=2, relief="solid")
output_text.pack(pady=10)

# Styling for buttons using ttk
style = ttk.Style()
style.configure("TButton",
                font=font_button,
                background="#4CAF50",
                foreground="black",  # Set text color to black
                padding=10)
style.map("TButton",
          background=[('pressed', '#45a049'), ('active', '#66bb6a')])

# Styling for the text box
style.configure("TText",
                background="#f7f7f7",
                foreground="black",
                fieldbackground="#f7f7f7",
                relief="solid")

# Start the GUI loop
root.mainloop()