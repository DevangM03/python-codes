def generate_substrings(s):
    # Base case: empty string
    if not s:
        return [""]  # only the empty substring

    # Recursive call for the rest of the string
    rest = generate_substrings(s[1:])

    # Start with all substrings of the rest
    result = rest.copy()

    # Add substrings that start with the current first character
    for sub in rest:
        if sub != "":  # avoid adding empty string again
            result.append(s[0] + sub)
    # Always add the single character as well
    result.insert(1, s[0])

    return result

# Test
print(generate_substrings("abc"))
