message = input("> ").lower()
words = message.split(" ")
emojis = {
    "love": "❤️",
    "cats": "🐱",
    "dogs": "🐶",
    "happy": "😊",
    "sad": "😢",
    "laugh": "😂",
    "love": "❤️",
    "cat": "🐱",
    "dog": "🐶",
    "fire": "🔥",
    "thumbs": "👍",
    "star": "⭐"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "

# Remove the trailing space and print the final result
print(output.strip())