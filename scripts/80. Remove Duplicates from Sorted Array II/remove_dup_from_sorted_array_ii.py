class Solution(object):
    def removeDuplicates(self, nums):
        d = {}
        k = 0
        redu = 0
        for i in range(len(nums)):
            if nums[i - redu] not in d:
                d[nums[i - redu]] = 1
            else:
                if d[nums[i - redu]] == 1:
                    d[nums[i - redu]] = 2
                else:
                    del [nums[i - redu]]
                    redu += 1
        
        return len(nums)