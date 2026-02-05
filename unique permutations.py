
def unique_permutation(s):
    if len(s) == 1:
        return[s]
    result = []
    for i in range(len(s)):
        if s[i] in s[:i]:
            continue
        char = s[i]
        remaining = s[:i] + s[i+1:]
        for perm in unique_permutation(remaining):
            result.append(char + perm)
    return result 
s = "abcca"
print(unique_permutation(s))
print(len(unique_permutation(s)))
