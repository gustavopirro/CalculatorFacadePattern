from controllers.average_calculator_controller import AverageCalculatorController
from views.average_calculator_view import AverageCalculatorView

def average_calculator_process():
    avg_calc_controller = AverageCalculatorController()
    avg_calc_view = AverageCalculatorView()

    initial_number_input = avg_calc_view.average_calculator_view()
    
    response = avg_calc_controller.get_average(initial_number_input)

    if response['success']:
        print(f"Resultado: { response['data'] }")