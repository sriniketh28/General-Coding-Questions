def twoSum(nums, target):
    dict = {}
    for i, num in enumerate(nums):
        if target-num in dict:
            return [dict[target-num], i]
        else:
            dict[num] = i

print(twoSum([3,3],6))
