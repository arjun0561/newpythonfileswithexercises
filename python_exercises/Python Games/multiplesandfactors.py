def find_factors_and_multiples():
    try:
        num = int(input("Enter a positive integer: "))

        if num <= 0:
            print('Please enter a positive integer')
            return 
    
        print(f"\nFactors of {num}: ")
        factors = [i for i in range(1, num + 1) if num % 1 == 0]
        print(factors)

        print(f"\nFirst ten multiples of {num}: ")
        multiples = [num * i for i in range(1, 11)]
        print(multiples)

    except ValueError:
        print("Please enter a valid positive integer")

find_factors_and_multiples()
