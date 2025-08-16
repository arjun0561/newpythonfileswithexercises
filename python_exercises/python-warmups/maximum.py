def find_max(numbers):
    maximum = numbers[0]  
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

print(find_max([4, 9, 2, 6]))  