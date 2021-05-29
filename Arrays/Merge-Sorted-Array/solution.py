def merge(nums1, m, nums2, n):
	m -= 1
	n -= 1
	while n >= 0:
		if m >= 0 and nums1[m] > nums2[n]:
			nums1[m+n+1] = nums1[m]
			m -= 1
		else:
			nums1[m+n+1] = nums2[n]
			n -= 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, 3, nums2, 3)
print(nums1)
