def check_even_odd(num):
    # if number is divisible by 2, remainder will be 0
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


# taking input from user
number = int(input("Enter a number: "))

# calling the function and sending the number
check_even_odd(number)