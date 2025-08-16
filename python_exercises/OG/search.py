text = input("Enter some text: ").lower()
search_ch = input("Enter the character you want to search for: ")

character_count = 0
for ch in text:
    if ch in search_ch:
        character_count += 1

print(f"The number of times {search_ch} is repeated in {text} is {character_count}.") 
