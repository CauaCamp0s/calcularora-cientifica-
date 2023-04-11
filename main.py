import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the entry widget
        self.entry = tk.Entry(master, width=40, justify="right")
        self.entry.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

        # Create the buttons
        buttons = [
            "7", "8", "9", "(", ")", "C",
            "4", "5", "6", "sin", "cos", "^",
            "1", "2", "3", "tan", "log", "sqrt",
            "0", ".", "+/-", "pi", "e", "/",
            "+", "-", "*", "%", "ln", "=",
        ]

        # Loop over the button list and create each one
        row = 1
        col = 0
        for button in buttons:
            def command(x=button): return self.handle_button_click(x)
            tk.Button(master, text=button, width=7, command=command).grid(
                row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 5:
                col = 0
                row += 1

    def handle_button_click(self, button):
        if button == "C":
            # Clear the entry widget
            self.entry.delete(0, tk.END)
        elif button == "=":
            # Evaluate the expression and display the result
            expression = self.entry.get()
            try:
                result = eval(expression)
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif button == "pi":
            # Insert the value of pi into the entry widget
            self.entry.insert(tk.END, str(math.pi))
        elif button == "e":
            # Insert the value of e into the entry widget
            self.entry.insert(tk.END, str(math.e))
        elif button == "sqrt":
            # Calculate the square root of the current entry and display the result
            expression = self.entry.get()
            try:
                result = math.sqrt(eval(expression))
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif button == "sin":
            # Calculate the sine of the current entry and display the result
            expression = self.entry.get()
            try:
                result = math.sin(math.radians(eval(expression)))
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif button == "cos":
            # Calculate the cosine of the current entry and display the result
            expression = self.entry.get()
            try:
                result = math.cos(math.radians(eval(expression)))
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif button == "tan":
            # Calculate the tangent of the current entry and display the result
            expression = self.entry.get()
            try:
                result = math.tan(math.radians(eval(expression)))
            except:
                result = "Error"
                self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif button == "^":
            # Raise the current entry to the power of the next number entered and display the result
            expression = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, expression + "**")
        elif button == "log":
            # Calculate the logarithm of the current entry and display the result
            expression = self.entry.get()
            try:
                result = math.log10(eval(expression))
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif button == "ln":
            # Calculate the natural logarithm of the current entry and display the result
            expression = self.entry.get()
            try:
                result = math.log(eval(expression))
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        elif button == "+/-":
            # Toggle the sign of the current entry
            expression = self.entry.get()
            if expression.startswith("-"):
                self.entry.delete(0)
                self.entry.insert(0, expression[1:])
            else:
                self.entry.insert(0, "-")
        elif button == "%":
            # Calculate the percentage of the current entry and display the result
            expression = self.entry.get()
            try:
                result = eval(expression) / 100
            except:
                result = "Error"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        else:
            # Add the button text to the end of the current entry
            self.entry.insert(tk.END, button)


root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
