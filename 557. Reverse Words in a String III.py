class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ") # splits sentence into words
        reversed_words = []
        
        for word in words:
            reversed_words.append(word[::-1]) # reverses the word
        
        return " ".join(reversed_words)
    
s = "Let's take LeetCode contest"

sol = Solution()
result = sol.reverseWords(s)

print(result)

