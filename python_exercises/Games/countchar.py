def count_characters():
    user_input = input("Enter a string: ").lower()
    find_char = input("What character(s) do you want to count: ")

    char_count = 0
    for char in user_input:
        if find_char in char:
            char_count += 1
    
    print(f"The character(s) amount in {user_input} is {char_count}")

count_characters()