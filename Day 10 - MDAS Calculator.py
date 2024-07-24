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


restart=True
while restart==True:
    clear()
    print(logo)
    
    n1 = float(input("What's the first number?: "))
    conti=True
    while conti:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        n2 = float(input("What's the second number?: "))
        #Solves inputs
        if operation=="+":
            result= add(n1,n2)
        elif operation=="-":
            result= subtract(n1,n2)
        elif operation=="*":
            result= multiply(n1,n2)
        elif operation=="/":
            result= divide(n1,n2)
        #Result
        print(f"{n1} {operation} {n2} = {result}") 
        
        #Continue or Restart
        conti=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if conti=="y":
            n1=result
        elif conti=="n":
            conti=False
            
                