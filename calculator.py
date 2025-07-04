def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose from +, -, *, /")

calculator()