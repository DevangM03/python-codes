def all_substrings(s):
    a = ""
    for i in range(len(s)):
        a = ""
        for j in range(i+1, len(s) + 1):
            a = a+s[j-1]
            print(a)
            
    
s = input()
all_substrings(s)

