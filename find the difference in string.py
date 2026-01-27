# function to find the extra letter
def find_added_letter(s, t):
    # loop through each character in string t
    for char in t:
        # if the character is not in s or its count in t is more than in s
        if t.count(char) != s.count(char):
            return char  # this is the extra letter

# example 1
s = "abcdefghijklmnop"
t = "dgacer"
print(find_added_letter(s, t))  
