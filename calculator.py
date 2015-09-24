"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    line = raw_input("> ")
    tokens = line.split(" ")
    
    if tokens[0] == "q":
        print "ending program"
        break
    

    else:
        operator = tokens[0]
        num1 = int(tokens[1])

        if len(tokens) > 2:
           num2 = int(tokens[2])

        if operator == "q":
            break
        elif operator == "+":
            print add(num1, num2)
        elif operator == "-":
            print subtract(num1, num2)
        elif operator == "*":
            print multiply(num1, num2)
        elif operator == "/":
            print divide(num1, num2)
        elif operator == "square":
            print square(num1)
        elif operator == "cube":
            print cube(num1)
        elif operator == "pow":
            print power(num1, num2)
        elif operator == "mod":
            print mod(num1, num2)
        else:
            print "I don't understand."
    


