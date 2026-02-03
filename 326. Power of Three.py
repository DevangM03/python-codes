class Solution(object):         

    def isPowerOfThree(self, n):

        # powers of 3 must be positive numbers
        if n <= 0: # if number is 0 or negative
            return False # it cannot be a power of 3 → stop here
        
        # keep dividing the number by 3 as long as it is divisible
        while n % 3 == 0: # % gives remainder. If remainder is 0, divisible by 3
            n = n // 3 # Divide n by 3 (// means integer division)
        
        # after dividing, check if we reached 1
        return n == 1 # if yes → True (it was a power of 3)
    
num = int(input("Enter a number: "))
sol = Solution()
print(sol.isPowerOfThree(num))