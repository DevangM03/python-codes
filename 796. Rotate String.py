def rotateString(s: str, goal: str) -> bool:
    # Length must be same
    if len(s) != len(goal):
        return False

    # Check if goal is inside s+s
    return goal in (s + s)

s = "abcde"
goal = "bcdea"

ret = rotateString(s, goal)
print(ret)
