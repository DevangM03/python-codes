class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # checks if every letter is capital
        if word.isupper():
            return True
        
        # checks if every letter is small
        elif word.islower():
            return True
        
        # first letter capital, rest small
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
    
word = "DevaNg"
sol = Solution()
print(sol.detectCapitalUse(word))
