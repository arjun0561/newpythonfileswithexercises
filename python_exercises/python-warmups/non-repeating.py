def find_non_repeating_char(text):
    text = ""
    answer = []
    for char in text.lower():
        if text[char] == 1:
            answer = char
    return answer

print(find_non_repeating_char("pythonpy"))