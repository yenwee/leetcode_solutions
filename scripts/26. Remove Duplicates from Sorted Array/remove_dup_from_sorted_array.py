class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Removing elements of an array inside a loop will mess up its index
        # Hence we set a static variable curr to keep track 
        curr = 1
        for i in range(len(nums)-1):
            if(nums[i] != nums[i+1]):
                # We put the unique element index + 1 in this loop.
                # Since the elements after k does not matter, we don't mind removing the elements after k.
                nums[curr] = nums[i+1]
                curr += 1
        return curr