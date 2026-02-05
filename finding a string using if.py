text = "I love python programming"
word = "pyt"

if word in text:
    # index() gives the starting position of the word
    print("Found at index", text.index(word))
else:

    print("Not found")
