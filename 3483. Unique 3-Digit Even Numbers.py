class Solution(object):
    def totalNumbers(self, digits):
        result = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or k == i:
                        continue
                    if digits[i] == 0:
                        continue
                    if digits[k] % 2 == 1:
                        continue
                    num = digits[i]*100 + digits[j]*10 + digits[k]
                    result.add(num)
        return len(result)

digits = [ 1, 2, 3, 4]
sol = Solution()
print(sol.totalNumbers(digits))
