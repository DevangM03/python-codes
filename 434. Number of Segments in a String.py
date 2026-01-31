class Solution:
    def NumberOfSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                count += 1
        return count 
    
# example 1 

s = "Breadth-First Search, it does not offer full, functional"

ret = Solution().NumberOfSegments(s)
print(ret) 
