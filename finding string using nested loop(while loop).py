sentence = "My name is Devang"
word = "Dev"

  # position in sentence
found = False  # tracks if word is found

while i < len(sentence):   # outer loop (checks each position)

    # checks first letter match
    if sentence[i] == word[0]:
        match = True
        j = 0  # position in word

        # inner loop (checks word letters)
        while j < len(word):
            
            
            if i + j >= len(sentence) or sentence[i + j] != word[j]:
                match = False
                break
            
            j += 1  # move to next letter of word

        
        if match:
            print("Word found at index", i)
            found = True  
            break

    i += 1  # move to next sentence position

# after checking whole sentence
if not found:
    print("Word not found")
