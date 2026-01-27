text = "I love python programming"
word = "l"

position = -1  # assume not found
# len(text) → total letters in the sentence
# len(word) → total letters in the word
# subtract because the word must fully fit inside the text
# +1 includes the last possible position
# so i becomes every possible starting index where the word could be
for i in range(len(text) - len(word) + 1): 
    if text[i:i+len(word)] == word: # comparison step
        position = i
        break
# text[i:i+len(word)] → takes a small part of the text 
# length of this part = length of the word
# we check if that slice equals the word
if position != -1:
    print("String found at index", position)
else:
    print("String not found")
