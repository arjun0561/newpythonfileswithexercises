def temperature_converter():
    Fahrenheit = input("Enter the amount of degrees Fahrenheit: ")
    Celsius = (int(Fahrenheit) - 32) * (5/9)
    print(f"The amount is {Celsius} degrees Celsius.")

temperature_converter()