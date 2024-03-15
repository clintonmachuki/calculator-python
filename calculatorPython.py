import tkinter as tk
import math

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def calculate():
    try:
        expression = entry.get().replace('^', '**')  # Replace ^ with ** for exponentiation
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def compute_function(func):
    try:
        value = float(entry.get())
        if func == 'sqrt':
            result = math.sqrt(value)
        elif func == 'log':
            if value > 0:
                result = math.log10(value)
            else:
                raise ValueError("Logarithm of a non-positive number")
        elif func == 'sin':
            result = math.sin(math.radians(value))
        elif func == 'cos':
            result = math.cos(math.radians(value))
        elif func == 'tan':
            result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError as ve:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: " + str(ve))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=6)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 1, 4), ('sqrt', 1, 5), ('log', 2, 4),
    ('sin', 2, 5), ('cos', 3, 4), ('tan', 3, 5),
    ('(', 4, 4), (')', 4, 5)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                           command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                           command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
                           command=lambda sym=text: button_click(sym))
    button.grid(row=row, column=col)

# Run the main loop
root.mainloop()
