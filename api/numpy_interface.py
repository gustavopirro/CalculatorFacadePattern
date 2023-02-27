import numpy as _np

class MathLibInterface:

    def average(self, numbers_array: list):
        try:
            result = _np.average(numbers_array)
            return self.__format_response(result)
        except Exception:
            return self.__generic_error()
    
    def variation(self, numbers_array: list):
        result = _np.average(numbers_array)
        return result
    
    def standard_deviation(self, numbers_array: list):
        result = _np.average(numbers_array)
        return result

    def __format_response(self, operation_result):
        return {'success': True, 'data':  operation_result}

    def __generic_error(self):
        return {'success': False, 'data': 'An error has ocurred' }