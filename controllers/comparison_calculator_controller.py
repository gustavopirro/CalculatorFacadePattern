from api.numpy_interface import MathLibInterface
import math

class ComparisonCalculatorController:
    
    def get_comparison(self, arr_data: float):
        variation_data = self._get_variation(arr_data)
        standard_deviation_data = self._get_standard_deviation(arr_data)
        result = self._data_comparison(variation_data, standard_deviation_data)
        
        return self._format_response(result)
    
    def _create_array(self, arr_data: float):
        return [math.pow(i * 11, 0.95) for i in arr_data]
    
    def _get_variation(self, arr_data: list):
        arr_variation = MathLibInterface().variation(arr_data)
        return arr_variation
    
    def _get_standard_deviation(self, arr_data: list):
        arr_standard_deviation = MathLibInterface().standard_deviation(arr_data)
        return arr_standard_deviation
    
    def _data_comparison(self, variation_data, standard_deviation_data):
        return variation_data > standard_deviation_data

    def _format_response(self, variation_is_gt_standard_deviation):
        if variation_is_gt_standard_deviation:
            return {'success': True, 'data': "Success! Variation is greater than average!"}
        return {'success': False, 'data': "The comparison failed... Variation must be greater than standard deviation!"}



