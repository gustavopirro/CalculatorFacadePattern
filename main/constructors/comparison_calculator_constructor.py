from controllers.comparison_calculator_controller import ComparisonCalculatorController
from views.comparison_calculator_view import ComparisonCalculatorView

def comparison_calculator_process():
    comparison_calc_controller = ComparisonCalculatorController()
    comparison_calc_view = ComparisonCalculatorView()

    initial_number_input = comparison_calc_view.comparison_calculator_view()
    
    response = comparison_calc_controller.get_comparison(initial_number_input)

    if response['success']:
        return comparison_calc_view._success_response(response)
    comparison_calc_view._fail_response(response)