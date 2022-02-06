class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums) - 3):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] * 4 > target:
                break

            for j in range(i + 1, len(nums) - 2):
            
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[i] + nums[j] * 3 > target:
                    break
                
                # Two pointer for two_sum problem
                l, r = j + 1, len(nums) - 1

                while l < r:
                    
                    curr = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr > target:
                        r -= 1
                    elif curr < target:
                        l +=  1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l, r = l + 1, r - 1
            
        return ans