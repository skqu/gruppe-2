from Lommeregner.EquationHistory import EquationHistory
from Lommeregner.Calculator import Calculator
from Lommeregner.GUI import GUI
import tkinter as tk

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
