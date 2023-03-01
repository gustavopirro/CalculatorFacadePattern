from controllers.average_calculator_controller import AverageCalculatorController


class TestController:

    def test_average_calculator_calculate_output(self):
        result = AverageCalculatorController().calculate(5)
        resultTwo = AverageCalculatorController().calculate(10)

        assert result['data'] == 4.904195753593585
        assert result['success']

        assert resultTwo['data'] == 6.470679039555207
        assert resultTwo['success']

    def test_average_calculator_wrong_input(self):
        result = AverageCalculatorController().calculate('a')
        assert result['success'] == False
        assert result['data'] == 'An error has ocurred'
