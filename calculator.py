from art2 import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# function= operations["+"]
# function(2,3)

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for x in operations:
        print(x)

    should_continue=True

    while should_continue:
        operation_symbol = input("pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.")
        if user_choice == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


