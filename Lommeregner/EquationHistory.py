import tkinter as tk
import tkinter.font as tkFont
import csv

class EquationHistory:
    def add_equation(self, equation, result):
        full_equation = f"{equation} = {result}\n"
        with open("data.csv", "a") as file:
            file.write(full_equation)

    def get_last_equations(self, count=10):
        with open("data.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)

        last_equations = [equation[0] for equation in lines[-count:]]
        return last_equations

    def show_last_equations(self, root, calculator, label_resultat):
        last_equations = self.get_last_equations()
        popupbox = tk.Toplevel(root)
        popupbox.geometry("+720+100")
        popupbox.resizable(False, False)
        button_font = tkFont.Font(family="arial", size=20, weight="bold")

        if last_equations:
            popupbox.title("Last Equations")

            for i, equation in enumerate(last_equations):
                text_width = button_font.measure(equation)
                button_width = max(20, text_width // 10)
                tk.Button(popupbox, text=equation, width=button_width, height=1, bg="#a8a625",
                          font=("arial", 20, "bold"),
                          command=lambda eq=equation: self.retrieve_equation(eq, calculator, label_resultat)).grid(
                    row=i, column=0, pady=2, sticky="ew")
        else:
            popupbox.title("Error")

            error_message = tk.Label(popupbox, text="\u26A0No equations found\u26A0", width=20, height=2, bg="red",
                                     font=("arial", 20, "bold"))
            error_message.pack(padx=5, pady=5)

            ok_button = tk.Button(popupbox, text="Ok", width=7, height=1, bg="lightblue", font=("arial", 16, "bold"),
                                  command=popupbox.destroy)
            ok_button.pack(padx=5, pady=5)

    def retrieve_equation(self, equation, calculator, label_resultat):
        calculator.equation = equation.split("=")[0].strip()
        label_resultat.config(text=calculator.equation)

    def clear_equations(self):
        with open("data.csv", "w") as file:
            file.truncate(0)

