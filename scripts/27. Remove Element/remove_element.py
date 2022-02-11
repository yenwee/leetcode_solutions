class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        
        for index in range(len(nums)):
            if nums[index] != val:
                nums[x] = nums[index]
                x += 1
        
        return x