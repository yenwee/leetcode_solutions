class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        self.backtrack(nums, [], stack)
        return stack
    
    def backtrack(self, nums, path, stack):
        stack.append(path)
        for index in range(len(nums)):
            self.backtrack(nums[index + 1:], path + [nums[index]], stack)