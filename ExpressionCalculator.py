class ExpressionSolver:
    def __init__(self):
        self.user_input = input("Enter the expression you want to solve: ")

    def printExpression(self):
        print(self.user_input)

    def CalculateExpression(self):
        try:
            self.value = eval(self.user_input)
        except:
            exit(code="An error has been detected in your expression.")
        print(self.value)


MyCalculator = ExpressionSolver()
MyCalculator.CalculateExpression()
