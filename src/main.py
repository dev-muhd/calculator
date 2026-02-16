# Validate first number
first_number = input("Enter the first number: ")

try:
    first_number = float(first_number)
except ValueError:
    print("Invalid input: please enter a numeric value (e.g. 10 or 3.5).")
    exit()

# Validate operator
selected_operator = input("Choose an operator (+, -, *, /): ")

if selected_operator not in ["+", "-", "*", "/"]:
    print("Invalid operator. Allowed operators are: + - * /")
    exit()

# Validate second number
second_number = input("Enter the second number:")

try:
    second_number = float(second_number)
except ValueError:
    print("Invalid input: please enter a numeric value (e.g. 10 or 3.5).")
    exit()

# Perform calculation based on the selected operator
if selected_operator == "+":
    calculation_result = first_number + second_number
    print(calculation_result)
elif selected_operator == "-":
    calculation_result = first_number - second_number
    print(calculation_result)
elif selected_operator == "*":
    calculation_result = first_number * second_number
    print(calculation_result)
elif selected_operator == "/":
    if second_number == 0:
        print("Math error: division by zero is not allowed.")
        exit()
    calculation_result = first_number / second_number
    print(calculation_result)