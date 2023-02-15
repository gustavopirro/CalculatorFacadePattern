from main.constructors.index_constructor import index_constructor
from main.constructors.average_calculator_constructor import average_calculator_process
def start_process():
    
    while True:
        user_choice = index_constructor()

        if user_choice == 1: average_calculator_process()
        elif user_choice == 2: pass
        elif user_choice == 3: pass