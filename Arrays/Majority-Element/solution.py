def majorityElement(nums):
	return sorted(nums)[len(nums)//2]

print(majorityElement([2,2,1,1,1,2,2]))
