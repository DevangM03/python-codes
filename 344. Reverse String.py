class Solution:
    def reverseString(self, s: list) -> None:
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


s = ["h","e","l","l","o","z"]

Solution().reverseString(s)  
print(s)  # prints the list itself
