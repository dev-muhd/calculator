number1 = input("Enter a number: ")
try:
    number1 = float(number1)
except ValueError:
    print("That's not a number!!")
    exit()
    
operator = input("Which operator: ")
if operator not in ["+", "-", "*", "/"]:
    print("Input a correct operator!!")
    exit()

number2 = input("Enter a number: ")
try:
    number2 = float(number2)
except ValueError:
    print("That's not a number!!")
    exit()

if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "*":
    result = number1 * number2
    print(result)
elif operator == "/":
    if number2 == 0:
        print("Cannot divide by zero")
        exit()
    result = number1 / number2
    print(result)
else:
    print("Input a correct operator!!")

