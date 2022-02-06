class Solution(object):
    def runningSum(self, nums):
        ans = [0] * len(nums)
        for i in range(0,len(nums)):
            ans[i] = sum(nums[0:i+1])
        return ans