from typing_extensions import IntVar
from art import logo
from replit import clear

#Add
def add(n1, n2):
    return n1 + n2
#Substract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2
    
operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    n1 = float(input("What's the first number?: "))
    conti=True
    while conti==True:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        n2 = float(input("What's the second number?: "))
        
        function_to_use = operations[operator]
        answer=function_to_use(n1,n2)
        
        print(f"{n1} {operator} {n2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") =="y":
            n1=answer
        else:
            conti=False
            clear()
            calculator()

calculator()