class AverageCalculatorView:

    def average_calculator_view(self):
        try:
            user_input = float(input('Insira o número inicial: '))
        except Exception:
            return user_input
        return user_input