class Solution(object):
    def twoSum(self, nums, target): # you don’t pass self manually
        # self -> object using this method (automatic)
        # nums -> list of numbers
        # target -> number we want to reach 
        seen = {} # create an empty dictionary

        for i in range(len(nums)): # loop through list using i 
            num = nums[i] # get current number from list and store it in num(variable)
            complement = target - num # finds the number needed to reach target

            if complement in seen: # checks if complement is in dictionary
                return [seen[complement], i] 
            else:
                seen[num] = i # if complement not found, stores current number

nums = [2,7,11,15]
target = 18

obj = Solution()              
result = obj.twoSum(nums, target)  
print(result)

