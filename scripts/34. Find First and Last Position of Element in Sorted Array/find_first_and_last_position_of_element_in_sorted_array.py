class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0; high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[low] == nums[high] == target:
                return [low, high]
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                if nums[low] != target: 
                    low += 1
                if nums[high] != target: 
                    high -= 1
        return [-1,-1]