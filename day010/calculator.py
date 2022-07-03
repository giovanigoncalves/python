from art import logo
import os

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {"+": add, 
              "-": sub, 
              "*": mult, 
              "/": div}

def calculator():
    os.system("clear")
    print(logo)

    n1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
        
    proceed = True
    while proceed:
        status_operation = False
        while not status_operation:
            sign = input("Pick an operation: ")
            if sign in operations.keys():
                status_operation = True
        
        n2 = float(input("What's the next number?: "))

        calc_function = operations[sign]
        res = calc_function(n1, n2)
        
        print(f"{n1:.1f} {sign} {n2:.1f} = {res:.1f}")

        should_continue = input(f"Type 'y' to continue calculating with {res:.1f}, or type 'n' to start a new calculation [crtl + c to exit]: ")
        if should_continue == 'y':
            n1 = res
        elif should_continue == 'n':
            proceed = False
            calculator()
        else:
            print("Invalid answer!")
            invalid = True
            while invalid:
                should_continue = input(f"Type 'y' to continue calculating with {res:.1f}, or type 'n' to start a new calculation [crtl + c to exit]: ")
                if should_continue == 'y':
                    n1 = res
                    invalid = False
                elif should_continue == 'n':
                    invalid = False
                    proceed = False
                    calculator()
                
calculator()
                
            
        