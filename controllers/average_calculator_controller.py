import math
from api.numpy_interface import MathLibInterface

class AverageCalculatorController:

    def get_average(self, number: float):
        try:
            new_arr = self.__create_array(number)
            r1 = self.__process_first_input(new_arr[0])
            r2 = self.__process_second_input(new_arr[1])
            
            data = [r1, r2, new_arr[2]]
            response = MathLibInterface().average(data)
            
            return self.__format_response(response, number)
        except:
            return { 'success': False, 'data': 'An error has ocurred' }

    def __create_array(self, number):
        return [number/3 for i in range(0,3)]
    
    def __process_first_input(self, input:float):
        CONST_NUMBER = 0.257
        return (math.sqrt(input + 7))/CONST_NUMBER
    
    def __process_second_input(self, input:float):
        return (math.pow(input, 2.121)/5)+1
    
    def __format_response(self, response, initial_input):
        return {'success': True, 'data': response, 'initial_input': initial_input, 'calculator': 'AverageCalculatorController'} 
    