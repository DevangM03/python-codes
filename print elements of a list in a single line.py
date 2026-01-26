cities = ["delhi", "noida", "gurgaon", "mumbai", "pune"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end= " ") 
        # end=" " adds a space instead of moving to a new line

print_list(cities)
print() # it's like pressing enter on a keyboard
print_len(cities)