INVALID_NUMBER_MSG = "Invalid input: please enter a numeric value (e.g. 10 or 3.5)."
INVALID_OPERATOR_MSG = "Invalid operator. Allowed operators are: + - * /"
DIVISION_BY_ZERO_MSG = "Math error: division by zero is not allowed."

def get_number(prompt_text, attempt=1):
    user_input = input(prompt_text)

    try:
        return float(user_input)
    except ValueError:
        if attempt < 2:
            return get_number(prompt_text, attempt + 1)
        else:
            print(INVALID_NUMBER_MSG)
            return None

def get_operator(attempt=1):
    operator = input("Choose an operator (+, -, *, /): ")

    if operator in ["+", "-", "*", "/"]:
        return operator
    elif attempt < 2:  
        return get_operator(attempt + 1)
    else:
        print(INVALID_OPERATOR_MSG)
        return None
        
        

def calculate(first_number, selected_operator, second_number):
    if selected_operator == "+":
        return first_number + second_number
    elif selected_operator == "-":
        return first_number - second_number
    elif selected_operator == "*":
        return first_number * second_number
    elif selected_operator == "/":
        if second_number == 0:
            print(DIVISION_BY_ZERO_MSG)
            return None
        return first_number / second_number
    

first_number = get_number("Enter the first number: ")
if first_number is None:
    exit()

selected_operator = get_operator()
if selected_operator is None:
    exit()

second_number = get_number("Enter the second number: ")
if second_number is None:
    exit()

calculation_result = calculate(first_number, selected_operator, second_number)

print(f"Result: {first_number} {selected_operator} {second_number} = {calculation_result}")