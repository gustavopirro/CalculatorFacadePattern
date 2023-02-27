class ComparisonCalculatorView:

    def comparison_calculator_view(self):
        user_array = []
        while True:
            message = """Insira um número para ser adicionado ao array.
digite f para finalizar o cálculo:"""
            user_input = input(message)
    
            if user_input == 'f':
                return user_array

            parsed_user_input = float(user_input)
            user_array.append(parsed_user_input)
        
    def _success_response(self, response):
        print("Resultado: ", response['data'])

    def _fail_response(self, response):
        print(response['data'])