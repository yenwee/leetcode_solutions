class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        res = 0
        for num in nums:
            res ^= num
            print(res)
        return res