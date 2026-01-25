s = "madan"      
rev = ""         # this empty box stores the word backwards

# We take each letter from the word one by one
for ch in s:
    rev = ch + rev   # puts the new letter in front of what we already saved

if s == rev:        
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
