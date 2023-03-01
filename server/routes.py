from flask import request, jsonify
from main.adapters.request_adapter import request_adapter
from controllers.average_calculator_controller import AverageCalculatorController
from controllers.comparison_calculator_controller import ComparisonCalculatorController
from controllers.variation_calculator_controller import VariationCalculatorController
from server.server import app


@app.route("/", methods=["GET"])
def health_test_view():
    return "API is up!"

@app.route("/avg", methods=["POST"])
def avg_calc_view():
    http_response = request_adapter(request, AverageCalculatorController())
    return jsonify(http_response.body), http_response.status_code 

@app.route("/var", methods=["POST"])
def var_calc_view():
    http_response = request_adapter(request, VariationCalculatorController())
    return jsonify(http_response.body), http_response.status_code 

@app.route("/comparison", methods=["POST"])
def comparison_calc_view():
    http_response = request_adapter(request, ComparisonCalculatorController())
    return jsonify(http_response.body), http_response.status_code 