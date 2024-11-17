def calculator():
    print("Welcome to the Basic Calculator!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers.")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    while True:
        operation = input("Enter your choice (1-4): ")
        if operation in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please try again.")
    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    print("Thank you for using the Basic Calculator!")
if __name__ == "__main__":
    calculator()
