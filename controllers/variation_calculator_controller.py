from api.numpy_interface import MathLibInterface
from controllers.interface.calculator_interface import CalculatorInterface
import math

class VariationCalculatorController(CalculatorInterface):
    
    def calculate(self, arr_data: float):
        try:
            new_array = self._create_array(arr_data)
            variation_data = self._apply_variation(new_array)
            return self._format_response(variation_data)
        except Exception as e:
            return {'success': False, 'data': f'An error ocurred: ${e}'}
    
    def _create_array(self, arr_data: float):
        return [math.pow(i * 11, 0.95) for i in arr_data]
    
    def _apply_variation(self, arr_data: list):
        arr_variation = MathLibInterface().variation(arr_data)
        return 1/arr_variation
    
    def _format_response(self, data):
        return {'success': True, 'data': data}



