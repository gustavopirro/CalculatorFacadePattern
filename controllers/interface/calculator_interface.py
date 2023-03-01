from abc import ABC, abstractmethod
from main.adapters.http_request import HttpRequest
from main.adapters.http_response import HttpResponse

class CalculatorInterface(ABC):

    @abstractmethod
    def calculate(self, input: HttpRequest) -> HttpResponse: 
        pass
