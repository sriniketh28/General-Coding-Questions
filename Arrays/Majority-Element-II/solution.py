from collections import Counter

def majorityElement(nums):
	return [key for key,value in Counter(nums).items() if value > len(nums)//3]

print(majorityElement([1,2]))
