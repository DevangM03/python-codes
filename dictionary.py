# creates a dictionary with subjects as keys and marks as values
marks = {"English" : 95, "Chemistry" : 98}
# access the value for the key "Chemistry" → prints 98
print(marks["Chemistry"])

marks["Physics"] = 97 # adds a new key "Physics" with value 97
print(marks) # prints updated dictionary

marks["Physics"] = 99 # updates the value of existing key "Physics" to 99
print(marks) # prints updated dictionary
