from api.numpy_interface import MathLibInterface
import math

class ComparisonCalculatorController:
    
    def get_comparison(self, arr_data: float):
        variation_data = self._get_variation(arr_data)
        average_data = self._get_average(arr_data)
        result = self._data_comparison(variation_data, average_data)
        return self._format_response(result)
    
    def _create_array(self, arr_data: float):
        return [math.pow(i * 11, 0.95) for i in arr_data]
    
    def _get_variation(self, arr_data: list):
        arr_variation = MathLibInterface().variation(arr_data)
        return arr_variation
    
    def _get_average(self, arr_data: list):
        arr_average = MathLibInterface().average(arr_data)
        return arr_average
    
    def _data_comparison(self, variation_data, average_data):
        return variation_data < average_data

    def _format_response(self, variation_is_gt_average):
        if variation_is_gt_average:
            return {'success': True, 'data': "Variation is greater than average!"}
        return {'success': False, 'data': "The comparison failed, variation must be greater than average!"}



