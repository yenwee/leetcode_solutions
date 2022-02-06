class Solution(object):
    def maxArea(self, nums):
        output = 0
        l, r = 0, len(nums) - 1
        while l < r: 
		    h = min(nums[l], nums[r]) 
		    w = r - l
		    area = h * w
		    output = max(area, output) 
		    if nums[l] < nums[r]: 
			    l += 1 
		    else:
			    r -= 1
    	return output