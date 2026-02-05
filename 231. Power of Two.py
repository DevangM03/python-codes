class Solution(object):
    def isPowerOfTwo(self, n) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2

        return n == 1
    
num = int(input("Enter a number: "))
sol = Solution()
print(sol.isPowerOfTwo(num))

