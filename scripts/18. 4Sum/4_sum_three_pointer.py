class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4 :
            return []
        
        nums.sort()
        ans = []
        for i in range(0, len(nums) -1): 
            if nums[i] * 4 > target :
                break
                    
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                 
            l , m , r = i + 1 , i + 2, len(nums) - 1
            while (i < l) and (l < m) and (m < r):
                curr = nums[i] + nums[l] + nums[m] + nums[r]
                
                if(curr == target):
                    if [nums[i] , nums[l] , nums[m] , nums[r]] not in ans:
                        ans.append([nums[i] , nums[l] , nums[m] , nums[r]])
                    m += 1
                    
                if (m < r) and (curr - target < 0):
                    while (nums[m] == nums[m + 1]) and (m < len(nums) - 2):
                        m += 1
                    m += 1
                    
                if (m < r) and (curr - target > 0):
                    while (nums[r] == nums[r - 1]) and (r > i):
                        r -= 1
                    r -= 1
                
                if (m >= r):
                    l += 1
                    m = l + 1
                    r = len(nums) - 1
                    
        return ans