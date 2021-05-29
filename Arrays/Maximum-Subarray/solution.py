def maxSubArray(nums):
	curr_max_sum = max_sum = nums[0]
	for num in nums[1:]:
		curr_max_sum = max(curr_max_sum+num, num)
		max_sum = max(curr_max_sum, max_sum)
	return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
