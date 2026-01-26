s = "hello"
ch = "e"

position = -1

for i in range(len(s)):
    if s[i] == ch:
        position = i
        break

print(position)
