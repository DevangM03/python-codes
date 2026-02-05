class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # convert string to list so we can change characters
        s = list(s)
        
        # move in steps of 2k
        for i in range(0, len(s), 2 * k):
            # reverse first k characters 
            s[i:i+k] = reversed(s[i:i+k])
        
        # convert list back to string
        return ''.join(s)

s = "afejncetng"
k = 3

sol = Solution()
result = sol.reverseStr(s, k)

print(result)
