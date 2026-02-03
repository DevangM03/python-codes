def generate_substrings(s):
    # Base case: empty string
    if not s:
        return [""]  # only the empty substring

    # Start with the first letter as a substring
    result = [s[0]]

    # Recursively get consecutive substrings of the rest of the string
    rest = generate_substrings(s[1:])

    # Add all consecutive substrings that start with the first letter
    for i in range(1, len(s)):
        result.append(s[0:i+1])  # s[0:i+1] is consecutive

    # Add substrings from the rest that do not include the first letter
    for sub in rest[1:]:  # skip the empty string because we already have it
        result.append(sub)

    # Always include the empty string at the beginning
    result.insert(0, "")

    return result

# Test
print(generate_substrings("abc"))
