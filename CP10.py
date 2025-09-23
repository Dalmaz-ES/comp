

def simple_calculator():

    #Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")


    #Perform the operation
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return "Error: Division by zero is not allowed." if num2 == 0 else num1 / num2
    else:
        return "Error: Invalid operator."
    

# Call the simple calculator function and print the result
result = simple_calculator()
print("Result:", result)