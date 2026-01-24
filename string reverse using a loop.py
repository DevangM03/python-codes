def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

original_string = "Devang Maurya"
result = reverse_string(original_string)
print("original string: ", original_string)
print("reversed string: ", result)