import tkinter as tk
from tkinter import ttk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()

        # Entry widget to display the result
        entry = ttk.Entry(root, textvariable=self.result_var, font=("Helvetica", 18), justify="right", state="disabled")
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=10)
        entry.bind("<Return>", lambda event: self.calculate())

        # Buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, column) in buttons:
            ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=column, sticky="nsew", ipadx=10, ipady=10)

        # Configure grid weights to make buttons expandable
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == "=":
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Concatenate the button text to the current text
            self.result_var.set(current_text + button_text)

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
