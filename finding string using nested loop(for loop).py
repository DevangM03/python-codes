sentence = "My name is Devang"
word = "angs" 
i = 0 
found = False

# loops through each position in the sentence
for i in range(len(sentence)):

    # checks if the current sentence letter matches
    # the first letter of the word
    if sentence[i] == word[0]:

        match = True   # assumes word matches for now

        # checks the rest of the letters in the word
        for j in range(len(word)):

            # if we go outside the sentence or letters don't match
            if i + j >= len(sentence) or sentence[i + j] != word[j]:
                match = False   
                break           

        
        if match:
            print("Word found at index", i)
            break   

# after checking whole sentence
if not found:
    print("Word not found")
