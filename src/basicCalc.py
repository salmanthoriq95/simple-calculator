# Basic menu
print("==============================")
print("|    Basic Calculator v1     |")
print("==============================")
print("| Operation:                  |")
print("| +  : multiply               |")
print("| /  : devide                 |")
print("| +  : add                    |")
print("| -  : minus                  |")
print("| ** : power                  |")
print("==============================")

# Input first number
num1 = input("Enter first number : ")
# validator and casting
try:
    if "." in num1 :
        num1 = float(num1)
    else :
        num1 = int(num1)
except ValueError:
    print("it is not a number")
    exit()
# Input second number
num2 = input("Enter second number : ")
# validator and casting
try:
    if "." in num2 :
        num2 = float(num2)
    else :
        num2 = int(num2)
except ValueError:
    print("it is not a number")
    exit()

# Operator input
value = 0
operation = input("Enter number of operation : ")
if operation == '*' :
     value = num1 * num2
elif operation == '/' :
     value = num1 / num2
elif operation == '+' :
     value = num1 + num2
elif operation == '-' :
     value = num1 - num2
elif operation == '**' :
     value = num1 ** num2
else :
    print('there is no such operator in menu')
    exit()

printOut = "{0} {1} {2} = {3}"
print(printOut.format(num1, operation, num2, value))