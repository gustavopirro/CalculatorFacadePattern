from flask import request as FlaskRequest
from main.adapters.http_request import HttpRequest
from main.adapters.http_response import HttpResponse
from controllers.interface.calculator_interface import CalculatorInterface

def request_adapter(request: FlaskRequest, calculator: CalculatorInterface) -> HttpResponse:
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_params=dict(request.args),
        path_params=request.view_args,
        url=request.full_path,
        ipv4=request.remote_addr,
    )

    print(http_request.body['value'])
    http_response = HttpResponse(200, calculator.calculate(http_request.body['value'])) 
    return http_response
