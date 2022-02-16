class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, white, end = 0, 0, len(nums)-1
        # Dutch Flag Partition Problem
        while white <= end:
            # If the white pointer is actually pointing at red object, swap their place instead
            if nums[white] == 0:
                nums[start], nums[white] = nums[white], nums[start]
                white += 1
                start += 1
                
            # If the white pointer is actually pointing at white object, move pointer forward
            elif nums[white] == 1:
                white += 1
                
            # If the white pointer is actually pointing at blue object, swap object with end of array object
            else:
                nums[white], nums[end] = nums[end], nums[white]
                end -= 1

                
        