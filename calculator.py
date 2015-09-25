"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

error_message = "I don't understand."
exception_message = "Please enter an operator followed by integers."

while True:
    line = raw_input("> ")
    tokens = line.split(" ")
    operator = tokens[0]
    
    if operator == "q":
        print "Goodbye!"
        break
    
    elif len(tokens) == 1:
        print error_message

    elif len(tokens) == 2:       
        try:
            num1 = int(tokens[1])       
        except ValueError:
            print exception_message
            continue

        if operator == "square":
            print square(num1)
        elif operator == "cube":
            print cube(num1)
        else:
            print error_message

    elif len(tokens) == 3:

        try:
            num1 = int(tokens[1])       
        except ValueError:
            print exception_message
            continue

        try:
            num2 = int(tokens[2])
        except ValueError:
            print exception_message
            continue

        if operator == "+":
            print add(num1, num2)
        elif operator == "-":
            print subtract(num1, num2)
        elif operator == "*":
            print multiply(num1, num2)
        elif operator == "/":
            print divide(num1, num2)
        elif operator == "pow":
            print power(num1, num2)
        elif operator == "mod":
            print mod(num1, num2)
        else:
            print error_message

    else:
        print error_message
    


