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