# Time complexity : O(n)
# Although the time complexity appears to be quadratic due to the while loop nested within the for loop, closer inspection reveals it to be linear.
def longestConsecutive(nums):
    nums_set = set(nums)
    ans = 0
    for num in nums_set:
        if num-1 not in nums_set:
            temp = num + 1
            while temp in nums:
                temp += 1
            ans = max(ans, temp-num)
            
    return ans

print(longestConsecutive([100,4,200,1,3,2]))

