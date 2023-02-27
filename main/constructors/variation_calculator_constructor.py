from controllers.variation_calculator_controller import VariationCalculatorController
from views.variation_calculator_view import VariationCalculatorView

def variation_calculator_process():
    var_calc_controller = VariationCalculatorController()
    var_calc_view = VariationCalculatorView()

    initial_number_input = var_calc_view.variation_calculator_view()
    
    response = var_calc_controller.get_variation(initial_number_input)

    if response['success']:
        return var_calc_view._success_response(response)
    var_calc_view._fail_response(response)