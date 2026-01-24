# input is a string by default
first = input("Enter first number : ")
operator = input("enter operator (+,-,*,/,%) : ")
second = input("Enter second number : ")
# converting the first and second numbers from string to integer
first = int(first)
second = int(second)

if operator == "+": # addition
    print(first + second)
    
elif operator == "-": # subtraction
    print(first - second)
    
elif operator == "*": # multiplication
    print(first * second)
    
elif operator == "/": # division
    print(first / second)
    
elif operator == "%": # remainder
    print(first % second)
    
else: # if none of the operators match
    print("Invalid operation")
# elif and else are dependent clauses that must follow an if statement
# cannot be used independently
