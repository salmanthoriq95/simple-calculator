import os

# Clear screen
def clrscr():
    os.system('cls')

# Border
def border(): 
    print("======================================")
    
# Header
def header() :
    border()
    print("|        Basic Calculator v1         |")
    border()

# Main menu
def mainMenu() :
    clrscr()
    header()
    print("| 1. Go to Calculator                |")
    print("| 2. How to                          |")
    print("| 3. Credit                          |")
    print("| 4. Exit                            |")
    border()

# How to use
def howTo() :
    clrscr()
    header()
    print("| How to use Calculator              |")
    border()
    print("| 1. Enter the first number          |")
    print("| 2. Enter the second number         |")
    print("| 3. Choose the operator             |")
    print("| 4. Value will be printed           |")
    print("| 5. enter the next number           |")
    print("|    if you want to operate          |")
    print("|    again, choose the operator      |")
    print("| 6. choose the operator again       |")
    print("| 7. if you want to exit,            |")
    print("|    enter anything except number    |")
    border()
    
# Credit
def credit():
    clrscr()
    header()
    print("| Credit                             |")
    border()
    print("| Author: Salman Thoriq              |")
    print("| Email : salmanthoriq95@gmail.com   |")
    border()

def operatorMenu():
    clrscr()
    header()
    print("| Operator :                         |")
    border()
    print("| * | Multiplication                 |")
    print("| / | Division                       |")
    print("| + | Addition                       |")
    print("| - | Substraction                   |")
    print("| ^ | exponen                        |")
    print("| v | Root                           |")
    print("| x | Exit to Main Menu              |")
    border()

# Number converter
def toNumber(num) :
    try:
        if "." in num :
            return float(num)
        else :
            return int(num)
    except ValueError:
        print("it is not a number")
        return False

# Operation
def operation() :
    num2 = 0
    value = 0
    operatorMath = ""
    printOut = "{0} {1} {2} = {3}"
    toMainMenu = False

    repeatFirstNumber = True
    while repeatFirstNumber :
        value = input("First number : ")
        if value.lower() == 'x':
            toMainMenu = True
            break
        value = toNumber(value)
        if value != False :
            repeatFirstNumber = False
    
    if toMainMenu :
        return

    repeatCalculate = True
    while repeatCalculate :
        num2 = input('Next number : ')
        if num2.lower() == 'x':
            break
        num2 = toNumber(num2)
        if num2 == False :
            repeatCalculate = True
            continue
        
        operatorMath = input("Operator : ")
        if operatorMath == '*' :
            num1 = value
            value = value * num2
            print(printOut.format(num1, operatorMath, num2, value))
            print("Previous value : {}".format(value))
            repeatCalculate = True
        elif operatorMath == '/' :
            num1 = value
            value = value / num2
            print(printOut.format(num1, operatorMath, num2, value))
            print("Previous value : {}".format(value))
            repeatCalculate = True
        elif operatorMath == '+' :
            num1 = value
            value = value + num2
            print(printOut.format(num1, operatorMath, num2, value))
            print("Previous value : {}".format(value))
            repeatCalculate = True
        elif operatorMath == '-' :
            num1 = value
            value = value - num2
            print(printOut.format(num1, operatorMath, num2, value))
            print("Previous value : {}".format(value))
            repeatCalculate = True
        elif operatorMath == '^' :
            num1 = value
            value = value ** num2
            print(printOut.format(num1, operatorMath, num2, value))
            print("Previous value : {}".format(value))
            repeatCalculate = True
        elif operatorMath == 'v' :
            num1 = value
            value = value ** (1/num2)
            print(printOut.format(num1, operatorMath, num2, value))
            print("Previous value : {}".format(value))
            repeatCalculate = True
        elif operatorMath.lower() == 'x':
            toMainMenu = True
            repeatCalculate = False
        else :
            print("Wrong Input!")
            repeatCalculate = True

    return toMainMenu
        

# Main Execution
repeatIt = True
while repeatIt :
    mainMenu()
    mainMenuinput = input("Enter number of menu : ")
    if mainMenuinput == '1':
        operatorMenu()
        operation()
        repeatIt = True
    elif mainMenuinput == '2':
        howTo()
        print("Press Enter to Main Menu : ")
        input()
        repeatIt = True
    elif mainMenuinput == '3':
        credit()
        print("Press Enter to Main Menu : ")
        input()
        repeatIt = True
    elif mainMenuinput == '4':
        print("Thankyou for using this app! Press enter to close the app")
        input()
        repeatIt = False
        clrscr()
        exit()
    else :
        print("Wrong input! Press Enter to continue")
        input()
        repeatIt = True


# # Input first number
# num1 = input("Enter first number : ")
# # validator and casting
# try:
#     if "." in num1 :
#         num1 = float(num1)
#     else :
#         num1 = int(num1)
# except ValueError:
#     print("it is not a number")
#     exit()
# # Input second number
# num2 = input("Enter second number : ")
# # validator and casting
# try:
#     if "." in num2 :
#         num2 = float(num2)
#     else :
#         num2 = int(num2)
# except ValueError:
#     print("it is not a number")
#     exit()

# # Operator input
# value = 0
# operation = input("Enter number of operation : ")
# if operation == '*' :
#      value = num1 * num2
# elif operation == '/' :
#      value = num1 / num2
# elif operation == '+' :
#      value = num1 + num2
# elif operation == '-' :
#      value = num1 - num2
# elif operation == '**' :
#      value = num1 ** num2
# else :
#     print('there is no such operator in menu')
#     exit()

# printOut = "{0} {1} {2} = {3}"
# print(printOut.format(num1, operation, num2, value))