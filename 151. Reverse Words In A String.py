class Solution(object):
    def reverseWords(self, s):
        words = s.split()      # split into words (no extra spaces)
        words.reverse()        # reverse the list
        return " ".join(words)

s = "the sky is blue"
sol = Solution()
result = sol.reverseWords(s)
print(result)
