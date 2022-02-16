class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        i = 0
        for color in [0,1,2]:
            if color in d:
                for replace in range(d[color]):
                    nums[i] = color
                    i += 1

                
        