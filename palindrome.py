# Check if a word is a palindrome
word = "radar"

# Compare the word with its reverse using slicing
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

