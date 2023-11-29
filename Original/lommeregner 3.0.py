import tkinter as tk
#import tkinter.messagebox as messagebox

class EquationHistory:
    def __init__(self):
        self.equation_history = []

    def add_equation(self, equation, result):
         full_equation = f"{equation} = {result}"
         self.equation_history.append(full_equation)

    def get_last_equation(self, count=5):
         return self.equation_history[-count:]

    def show_last_equations(self, root, calculator, label_resultat):
        last_equations = self.get_last_equation()
        if last_equations:
            popupbox = tk.Toplevel(root)
            popupbox.title("Last Equations")
            for i, equation in enumerate(last_equations):
                 tk.Button(popupbox, text=equation, width=40, height=2, bg="#a8a625", font=("arial", 16, "bold"), command=lambda eq=equation: self.retrieve_equation(eq, calculator, label_resultat)).grid(row=i, column=0, pady=5)
        else:
          popupbox = tk.Toplevel(root)
          popupbox.title("Error")
          popupbox.resizable(False, False)
          error_message = tk.Label(popupbox, text="\u26A0No equations found\u26A0", width=20, height=2, bg="red", font=("arial", 16, "bold"))
          error_message.pack(padx=5, pady=5)

          ok_button = tk.Button(popupbox, text="Ok", width=7, height=1, bg="lightblue", font=("arial", 16, "bold"), command=popupbox.destroy)
          ok_button.pack(padx=5, pady=5)

        #else:
        #    tk.messagebox.showerror("Error", "No equations found")

    def retrieve_equation(self, equation, calculator, label_resultat):
        calculator.equation = equation.split("=")[0].strip()
        label_resultat.config(text=calculator.equation)

    def clear_equations(self):
        return self.equation_history.clear()

class Calculator:
    def __init__(self, equation_history):
        self.equation = ""
        self.result = None
        self.equation_history = equation_history

    def addition(self, value):
        self.equation += value

    def subtraction(self, value):
        self.equation += value

    def multiply(self, value):
        self.equation += value

    def divide(self, value):
        self.equation += value

    def calculate(self):
        if self.equation:
            try:
                self.result = str(eval(self.equation))
                self.equation_history.add_equation(self.equation, self.result)
            except:
                self.result = "Error"
            self.equation = ""
        else:
            self.result = "Error"

    def clear(self):
        self.equation = ""
        self.result = ""


class GUI:
    def __init__(self, root, calculator, equation_history):
        self.root = root
        self.root.title("Lommeregner")
        self.calculator = calculator
        self.equation_history = equation_history
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        self.create_gui()

    def create_gui(self):
        self.label_resultat = tk.Label(self.root, width=25, height=2, text="", bg="black", fg="green", borderwidth=5, relief="solid", font=("arial", 30, "bold"))
        self.label_resultat.grid(row=0, column=0, columnspan=4, pady=(0, 10))


        # Create buttons using grid layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("-", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("+", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("/", 4, 3),
            ("Delete History", 5, 0), ("History", 5, 2)
        ]

        for (text, row, column) in buttons:
            if text == "=":
                tk.Button(self.root, text=text, width=5, height=1, bg="green", font=("arial", 28, "bold"),
                          command=self.on_calculate_click).grid(row=row, column=column, padx=0, pady=0, sticky="news")
            elif text == "C":
                tk.Button(self.root, text=text, width=5, height=1, bg="red", font=("arial", 28, "bold"),
                          command=self.on_clear_click).grid(row=row, column=column, padx=0, pady=0, sticky="news")
            elif text == "History":
                tk.Button(self.root, text="History", width=11, height=1, bg="#1b1bf5", font=("arial", 28, "bold"),
                          command=lambda: self.equation_history.show_last_equations(self.root, self.calculator, self.label_resultat)).grid(row=row, column=column, columnspan=2, padx=0, pady=0, sticky="new")
            elif text == "Delete History":
                tk.Button(self.root, text="Delete History", width=11, height=1, bg="darkred", font=("arial", 28, "bold"),
                          command=lambda: self.equation_history.clear_equations()).grid(row=row, column=column, columnspan=2, padx=0, pady=0, sticky="new")
            else:
                tk.Button(self.root, text=text, width=5, height=1, bg="#f2ff00", font=("arial", 30),
                          command=self.on_button_click(text)).grid(row=row, column=column, padx=0, pady=0, sticky="ew")

    def show(self, value):
        self.calculator.addition(value)
        self.label_resultat.config(text=self.calculator.equation)

    def on_button_click(self, value):
        def handler():
            self.show(value)

        return handler

    def on_calculate_click(self):
        self.calculator.calculate()
        self.label_resultat.config(text=self.calculator.result)

    def on_clear_click(self):
        self.calculator.clear()
        self.label_resultat.config(text="")

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.equation_history = EquationHistory()
        self.calculator = Calculator(self.equation_history)
        self.gui = GUI(self.root, self.calculator, self.equation_history)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Main()
    app.run()