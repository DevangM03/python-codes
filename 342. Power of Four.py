class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        while n % 4 == 0:
            n = n // 4

        return n == 1
    
num = int(input("Enter a number: "))
sol = Solution()
print(sol.isPowerOfFour(num))