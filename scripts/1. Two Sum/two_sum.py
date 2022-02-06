class Solution(object):
    def twoSum(self, nums, target):
        for idx, val in enumerate(nums):
            diff = target - val
            try:
                if (diff in nums) & ~(idx == nums.index(diff)):
                    num_one = idx
                    num_two = nums.index(diff)
                    break
            except:
                pass
        return num_one , num_two