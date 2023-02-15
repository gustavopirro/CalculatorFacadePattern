import numpy as _np

class MathLibInterface:

    def average(self, numbers_array: list):
        try:
            self.__input_validation(numbers_array)
            result = _np.average(numbers_array)
            return self.__format_response(result)
        except:
            return self.__generic_error()
    
    def variation(self, numbers_array: list):
        try:
            self.__input_validation(numbers_array)
            result = _np.average(numbers_array)
            return self.__format_response(result)
        except:
            return self.__generic_error()
    
    def standard_deviation(self, numbers_array: list):
        try:
            self.__input_validation(numbers_array)
            result = _np.average(numbers_array)
            return self.__format_response(result)
        except:
            return self.__generic_error()
    
    def __input_validation(self, input_data):
        assert type(input_data) == list

    def __format_response(self, operation_result):
        return {'success': True, 'data':  operation_result}

    def __generic_error(self):
        return {'success': False, 'data': 'An error has ocurred' }