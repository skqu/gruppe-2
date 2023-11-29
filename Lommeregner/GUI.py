import tkinter as tk
class GUI:
    def __init__(self, root, calculator, equation_history):
        self.root = root
        self.root.title("Lommeregner")
        self.calculator = calculator
        self.equation_history = equation_history
        self.root.configure(bg="white")
        self.root.resizable(False, False)
        self.create_gui()
        self.root.geometry("+100+100")

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
