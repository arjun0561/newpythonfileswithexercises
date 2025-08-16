def fibonacci():
    # Initialize the first two numbers in the sequence
    first_number = 0
    second_number = 1
    
    print("Fibonacci sequence:")
    print(first_number)  # Print the first number
    
    for i in range(10):
        # Calculate the next number in the sequence
        next_number = first_number + second_number
        print(next_number)
        
        # Update the numbers for the next iteration
        first_number = second_number
        second_number = next_number

fibonacci()