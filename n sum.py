def nSum(nums, p, N, target):
    result = []
    if p >= len(nums):
        return None
    if N <= 0 or target <= 0:
        return None
    if N == 1 and target == nums[p]:
        return [[target]]
    result = nSum(nums, p+1, N, target)
    result2 = nSum(nums, p+1, N-1, target - nums[p])
    if result2:
        for i in range(len(result2)):
            result2[i].append(nums[p])
        if result:
            result = result + result2
        else:
            result = result2
    return result


nums = [5, 6, 1, 4, 3, 2]


print(nSum(nums, 0, 4, 12))