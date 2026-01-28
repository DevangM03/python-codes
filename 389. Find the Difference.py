class Solution:
    def findTheDifference(self, s, t):
        # loop through each character in string t
        for char in t:
            # if the count in t is different from s, that's the extra letter
            if t.count(char) != s.count(char):
                return char

# example usage
s = "devang"
t = "anvdzge"

# call the method using the class
ret = Solution().findTheDifference(s, t)
print(ret) 