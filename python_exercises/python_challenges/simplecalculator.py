def calculator():
    print("Welcome to the Basic Calculator!")
    print("Operations: +, -, *, /")
    print("Enter 'q' to quit.")

    while True:
        # Get user input
        num1 = input("Enter first number: ")
        if num1.lower() == 'q':
            break
        num2 = input("Enter second number: ")
        if num2.lower() == 'q':
            break
        operation = input("Choose operation (+, -, *, /): ")
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    print("Try again.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation! Please try again.")
                continue
            
            print(f"Result: {result}")
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        option = input("Do you want to quit (y/n)? ").lower()
        if option == 'y':
            break
        else:
            print("Restarting Calculaator...")
            continue

    print("Thank you for using the calculator!")

# Run the calculator
calculator()