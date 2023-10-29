import tkinter as tk

class Calculator:
    def __init__(self):
        self.equation = ""
        self.result = None

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
            except:
                self.result = "Error"
            self.equation = ""
        else:
            self.result = "Error"

    def clear(self):
        self.equation = ""
        self.result = ""


class GUI:
    def __init__(self, root, calculator):
        self.root = root
        self.root.title("Lommeregner")
        self.calculator = calculator
        self.root.configure(bg="#a8a625")
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
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("/", 4, 3)
        ]

        for (text, row, column) in buttons:
            if text == "=":
                tk.Button(self.root, text=text, width=5, height=1, bg="blue", font=("arial", 28, "bold"),
                          command=self.on_calculate_click).grid(row=row, column=column)
            elif text == "C":
                tk.Button(self.root, text=text, width=5, height=1, bg="red", font=("arial", 28, "bold"),
                          command=self.on_clear_click).grid(row=row, column=column)
            else:
                tk.Button(self.root, text=text, width=5, height=1, bg="#f2ff00", font=("arial", 30),
                          command=self.on_button_click(text)).grid(row=row, column=column)

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
        self.calculator = Calculator()
        self.gui = GUI(self.root, self.calculator)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Main()
    app.run()