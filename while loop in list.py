marks = [95, 98, 97]

i = 1 # initializes index (counter) to 1 instead of 0
# A counter variable is a variable used to keep track of how many times a loop has run 
# or which element you’re currently at.

while i < len(marks): # loop runs as long as index is less than the length of the list
    print(marks[i]) # prints the element at the current index
    i = i + 1 # increments index by 1 to move to the next element

marks.clear()
print(marks)
