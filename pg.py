import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

def on_generate():
    try:
        min_length = int(length_entry.get())
        numbers = num_var.get()
        specials = special_var.get()
        if min_length < 1:
            messagebox.showerror("Invalid input", "Length must be at least 1")
            return
        password = generate_password(min_length, numbers, specials)
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for length")

# Set up GUI window
root = tk.Tk()
root.title("Password Generator")

# Password length input
tk.Label(root, text="Minimum Length:").grid(row=0, column=0, sticky="w")
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Numbers checkbox
num_var = tk.BooleanVar(value=True)
num_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=num_var)
num_checkbox.grid(row=1, column=0, columnspan=2, sticky="w")

# Special characters checkbox
special_var = tk.BooleanVar(value=True)
special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_var)
special_checkbox.grid(row=2, column=0, columnspan=2, sticky="w")

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=3, column=0, columnspan=2)

# Result display
result_var = tk.StringVar()
tk.Label(root, text="Generated Password:").grid(row=4, column=0, sticky="w")
result_label = tk.Entry(root, textvariable=result_var, width=40)
result_label.grid(row=4, column=1)

root.mainloop()
